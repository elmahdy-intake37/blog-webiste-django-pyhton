from django import forms
from .models import Comment,Reply,Post,category,forbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#post
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('comment_contant',)

class ReplayForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('reply_contant',)

#admin
def clean_message(self):
	message = self.clean_data.get('message', '')
	num_words = len(message.split())
	if num_words < 4:
		raise forms.ValidationError("Not enough words!")
	return message	

def clean_data(self):
	message = self.clean_data.get('message', '')
	num_words = len(message.split())
	if num_words < 4:
		raise forms.ValidationError("Not enough words!")
	return messag

class PostFrom(forms.ModelForm):
	class Meta:
			model = Post
			fields=('title', 'contant', 'post_category','post_time')	

class CreationForm(UserCreationForm):
	class Meta:
		model = User	
		fields=['username','email','password1','password2']

class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','password1','password2']

class ChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2','email']

class CategorytForm(forms.ModelForm):
	class Meta:
		model = category
		fields=['id','title']

class RudeForm(forms.ModelForm):
	class Meta:
		model = forbidden
		fields=['rude_words']


		
