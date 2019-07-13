from django import forms

from .models import AuthUser
from django.contrib.auth import(

authenticate,
get_user_model,
login,
logout,

)


User = get_user_model()

class UserForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields = ('username', 'is_superuser', 'is_active',)

class UserLoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):

		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		user=authenticate(username=username,password=password)

		if not user:

			raise forms.ValidationError("This user doesn't exist")

		if not user.check_password(password):
			raise forms.ValidationError("Incorrect password")

		if not user.is_active:
			raise forms.ValidationError("This user isn't active")


		return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRegisterForm(forms.ModelForm):
	email=forms.EmailField(label="Email")
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(widget=forms.PasswordInput,label="Confirm password")
	class Meta:
		model = User
		fields=[
				'username',
				'email',
				'password',
                'password2',
			]

	def clean_password2(self):
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Passwords don't match")
		email_qs=User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email is already exists")
		#username_qs=User.objects.filter(username=username)
		#if username_qs.exists():
		#	raise forms.ValidationError("Username is already exists")
		return password
