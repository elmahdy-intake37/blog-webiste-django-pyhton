from django.shortcuts import render, get_object_or_404,redirect
from .models import category, Post,Comment ,Reply,forbidden
from django.http import HttpResponse ,HttpResponseRedirect
from forms import CommentForm ,ReplayForm ,PostFrom, CreationForm,CategorytForm,RudeForm
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def show_all_categorys(request):
	all_cat = category.objects.all()
	current_user = request.user
	allsubscribe= category.objects.filter(user = current_user)
	context = {'all_categorys': all_cat,'allsubscribe':allsubscribe}
	return render(request, 'geeks/index.html' ,context)

def show_all_body(request):
	all_post = Post.objects.all().order_by('post_time').reverse()
	context = {'all_posts': all_post}
	return render(request, 'geeks/show_all_posts.html' ,context)

def show_posts(request,id):
	all_post = Post.objects.filter(post_category=id).order_by('post_time').reverse()
	context = {'all_posts': all_post}
	return render(request, 'geeks/show_all_posts.html' ,context)

def details(request,id):
	post = Post.objects.get(id=id)
	all_comments=Comment.objects.filter(post_comment_id=id)
	all_replay=Reply.objects.filter(post_id=id)
	context = {'spacific_post':post,'all_comments':all_comments,'all_replay':all_replay}
	return render(request, 'geeks/show_post.html' ,context)

# def new_comment(request,id):
# 	post = get_object_or_404(Post, id=id)
# 	if request.method == "POST":
# 		form = CommentForm(request.POST)
# 		if form.is_valid():
# 			comment = form.save(commit=False)
# 			comment.post_comment_id_id = id
# 			comment.save()
# 			return HttpResponseRedirect("/geeks/posts/"+id+"/details")#details(request,id)
# 	else:
# 		form = CommentForm()
#     	return render(request, 'geeks/new_comment.html', {'form': form})

def new_comment(request,id):
	post = get_object_or_404(Post,id=id)
	user_id=request.user.id
	print id
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post_comment_id_id = id
			comment.author_id=int(user_id)
			comment.check_func()
			return details(request,post.id)
	else:
		form = CommentForm()
    	return render(request, 'geeks/new_comment.html', {'form': form})

def new_reply(request,postid,commentid):
	post = get_object_or_404(Post, id=postid)
	comment = get_object_or_404(Comment, id=commentid)
	user_id=request.user.id
	if request.method == "POST":
		form = ReplayForm(request.POST)
		if form.is_valid():
			reply = form.save(commit=False)
			reply.post_id_id = postid
			reply.author_id=int(user_id)
			reply.comment_id_id = commentid
			reply.check_func()
			return HttpResponseRedirect("/geeks/posts/"+postid+"/details")
	else:
		form = ReplayForm()
    	return render(request, 'geeks/new_reply.html', {'form': form})


#admmin
def show_allcategorys(request):
	all_cat = category.objects.all()
	context = {'all_categorys': all_cat}
	return render(request, 'adminuser/conrolercategory.html' ,context)

def show_posts(request,id):
	all_post = Post.objects.filter(pk=id)
	context = {'all_posts': all_post}
	return render(request, 'adminuser/show_all_posts.html' ,context)

def details(request,id):
	post = Post.objects.get(id=id)
	context = {'spacific_post':post}
	return render(request, 'adminuser/show_post.html' ,context)
def edit_category(request, id):
	st = category.objects.get(pk= id)
	form =CategorytForm(instance = st)
	if request.method == 'POST':
		form = CategorytForm(request.POST, instance=st)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/adminuser/category')

	context = {'cnew_form': form}
	return render(request, 'adminuser/category_form.html',context)




def category_new(request):

	form= CategorytForm()
	if request.method == 'POST':
		form = CategorytForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/adminuser/category')
	context={'cnew_form':form}
	return render(request, 'adminuser/category_form.html', context)

def del_category(request, id):
	st = category.objects.get(id=id)
	st.delete()
	return HttpResponseRedirect('/geeks/adminuser/category')

def details_category(request,id):
	cat=category.objects.get(pk=id)
	all_cat=category.objects.filter(pk=id)
	context = {'all_cat':all_cat,'cat':cat}
	return render(request, 'adminuser/detail_cat.html' ,context)
##############################################

def contact(request):
	form=ContactForm()
	if request.method == 'POST':
		form =ContactForm(request.POST)
		if form.is_valid():
			topic = form.cleaned_data['topic']
			message=form.cleaned_data['message']
			sender=form.cleaned_data['sender']

			# sender=form.cleaned_data.get['sender','bassant.a.abdelfattah@gmail.com']
			send_mail(
				'Feedback from your site, topic: %s' % topic,
				message, sender,
				['elmahdy30@gmail.com'],
				 auth_user='elmahdy30@gmail.com', auth_password="yarab1234"

				)
			#form.save()
			return HttpResponseRedirect('/geeks')
	context={'contact_form':form}
	"""else:
			form=ContactForm()"""
	return render(request,'admin/contact.html',context)

	#CRUD for user

def Post_new(request):

	form= PostFrom()
	if request.method == 'POST':
		form = PostFrom(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/adminuser/post')
	context={'pnew_form':form}
	return render(request, 'adminuser/Post_form.html', context)

def Posts_delete(request, id):

	p=Post.objects.get(pk=id)
	p.delete()
	return HttpResponseRedirect('/geeks/adminuser/post')

def Post_update(request, id):
	P = Post.objects.get(pk=id)
	form = PostFrom(instance = P)
	if request.method == 'POST':
		form = PostFrom(request.POST, instance=P)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/adminuser/post')



	context = {'pnew_form': form}
	return render(request, 'adminuser/Post_form.html',context)

def showall_post(request):
	all_post = Post.objects.all()
	context = {'all_post': all_post}
	return render(request, 'adminuser/controleronpost.html' ,context)

#////// for autho

"""def login(request):
	user_name = request.POST['user_name']
	passwd = request.POST['passwd']
	user = auth.authenticate(user_name=username, passwd=password)
	if user is not None and user.is_active:
	# Correct password, and the user is marked "active"
		auth.login(request, user)
	# Redirect to a success page.
		return HttpResponseRedirect("/account/loggedin/")
	else:
	# Show an error page
		return HttpResponseRedirect("/account/invalid/")

#for logo out
def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/account/loggedout/")


	#  regestrion
def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		data = request.POST.copy()
		errors = form.get_validation_errors(data)
		if not errors:
			new_user = form.save(data)
			return HttpResponseRedirect("/books/")
	else:
		data, errors = {}, {}
		return render_to_response("registration/register.html", {
		'form' : forms.FormWrapper(form, data, errors)
})"""

#class admin(request):
#creating username
###done
def create_user(request):
	form=CreationForm()
	if request.method == 'POST':
	 	form=CreationForm(request.POST)
	 	if form.is_valid():
	 		form.save()
	 		return HttpResponseRedirect('goo')
	context={'form':form}

	return render(request,'adminuser/createuser.html', context)





	###############done

def update(request,id):
	u=User.objects.get(pk=id)
	form=ProfileForm(instance = u)
	if request.method == 'POST':
		form = ProfileForm(request.POST,instance=u)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks')
	context = {'pdate_form': form}
	return render(request,'adminuser/updateuser.html', context)







#############done
def change(request):
	c=request.user
	form=ChangeForm(instance=c)
	if request.method == 'POST':
		form=ChangeForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks')
	context = {'change_form': form}
	return render(request, 'adminuser/changepasswordh.html', context)

####done

def del_user(request, id):

		u = User.objects.get(pk = id)
		u.delete()
		#messages.sucess(request, "The user is deleted")
		return render(request, 'adminuser/controleronuser.html' )
####done
def show_one_user(request,id):
	userers = User.objects.get(pk=id)
	usfilter=User.objects.filter(pk=id)
	context={
	'user':userers,
	'usfilte':usfilter
	}

	return render(request, 'adminuser/show_one_user.html' ,context)


##done
def show_all_user(request):
	all_user = User.objects.all()
	context = {'all_user': all_user}
	return render(request, 'adminuser/controleronuser.html' ,context)


def adminhome(request):
	return render(request,'adminuser/adminlink.html')

def categ(request):

	return render(request,'adminuser/controleronuser.html')

def select_word(request):
	rude = forbidden.objects.all()
	context = {'rude': rude}
	return render(request, 'geeks/showallrude.html' ,context)

def create_word(request):
	form= RudeForm()
	if request.method == 'POST':
		form = RudeForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/allcategorys')
	context={'create_word':form}
	return render(request, '/geeks/createword.html', context)

def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    return HttpResponseRedirect('/geeks/allcategorys')

def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/geeks/allcategorys')
