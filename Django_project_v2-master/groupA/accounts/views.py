from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from django.contrib.auth.views import login
from django.contrib.auth import(

authenticate,
get_user_model,

logout,


)

from .models import AuthUser
from .forms import UserLoginForm,UserRegisterForm,UserForm



#/def login_view(request):

#/	title="login"

#/	form=UserLoginForm(request.POST or None)

#/	if form.is_valid():

		#return render(request,"form.html",{"form":form,"title":title,})
#/		username=form.cleaned_data.get("username")
#/		password=form.cleaned_data.get("password")

#/		user=authenticate(username=username,password=password)
#/		if request.user.is_authenticated():
#/		        login(request,user)
#/                return redirect("/admin/")
                #if not request.user.is_superuser:
		#	return redirect("/admin")

		#else:
		#return redirect("/login/")

		#else:

		#return HttpResponse("not valide")
			#return redirect("/registration/")



#/	return render(request,"form.html",{"form":form,"title":title,})
def login_view(request):
	if not request.user.is_authenticated():

		return login(request)

        else:

		if request.user.is_superuser:
			return redirect("/geeks/mainpage")

		else:
		#return redirect("/login/")
		#return redirect("/admin/")
                	return HttpResponseRedirect('/geeks/mainpage')#render(request,"test.html",{})



#def logout_view(request):

#	logout(request)
 #       return redirect("/login/")


def register_view(request):

	title="Registeration"

	form=UserRegisterForm(request.POST or None)

	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
                return redirect("/accounts/home/")

	return render(request,"register.html",{"form":form,"title":title,})



def edit(request, idd):
	#return HttpResponse("tes")
	student = get_object_or_404 (AuthUser, id=idd)
	form = UserForm(instance=student)
	if request.method == "POST":
		form = UserForm( request.POST, instance=student)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/accounts/show')
        
	return render(request, 'editUsers.html', {'form':form})




def show(request):

	alltable=AuthUser.objects.all()

	return render(request,"users_table.html",{"tables":alltable,})

