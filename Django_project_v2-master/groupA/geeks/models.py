from django.db import models
from datetime import datetime
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# class category(models.Model):
# 	title=models.CharField(max_length=200)
# 	def __str__(self):
# 		return self.title
# 	def was_published_recently(self):
#  		return date.today() > self.post_time.date()
#
# 	was_published_recently.short_description = 'Puplished Before Today ?'
#  	was_published_recently.boolean = True
#
# 	def __str__(self):
# 		return self.title

class category(models.Model):
	title=models.CharField(max_length=200)
	user = models.ManyToManyField(User, blank=True)
	def __str__(self):
		return self.title
	def was_published_recently(self):
 		return date.today() > self.post_time.date()

	was_published_recently.short_description = 'Puplished Before Today ?'
 	was_published_recently.boolean = True

	def __str__(self):
		return self.title


class Post(models.Model):
	title=models.CharField(max_length = 200)
	contant=models.TextField()
	post_category=models.ForeignKey(category,on_delete=models.CASCADE)
	post_time=models.DateTimeField(default=datetime.now())
	post_image = models.ImageField(upload_to = "img/geeks",default='img/geeks/No_Image.jpg')
	def __str__(self):
		return '%s %s'%(self.title, self.post_category)

# class Comment(models.Model):
# 	comment_contant=models.TextField()
# 	comment_date=models.DateTimeField(default=datetime.now())
# 	post_comment_id=models.ForeignKey(Post,on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.comment_contant
class Comment(models.Model):
	comment_contant=models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment_date=models.DateTimeField(default=datetime.now())
	post_comment_id=models.ForeignKey(Post,on_delete=models.CASCADE)
	def __str__(self):
		return self.comment_contant

	def check_func(self):
		bad_words=forbidden.objects.all()
		temp=""
		commentcheck=self.comment_contant.split()
		for word in commentcheck:
			for bad in bad_words:
				if word == bad.rude_words:
					word=len(word)*"*"
					break
			temp+=" "
			temp+=word
		self.comment_contant=temp
		self.save()


class Reply(models.Model):
	reply_contant=models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	reply_date=models.DateTimeField(default=datetime.now())
	post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
	comment_id=models.ForeignKey(Comment,on_delete=models.CASCADE)

	def __str__(self):
		return self.reply_contant

	def check_func(self):
		bad_words=forbidden.objects.all()
		temp=""
		replycheck=self.reply_contant.split()
		for word in replycheck:
			for bad in bad_words:
				if word == bad.rude_words:
					word=len(word)*"*"
					break
			temp+=" "
			temp+=word
		self.reply_contant=temp
		self.save()

class forbidden(models.Model):
	rude_words=models.TextField()
	def __str__(self):
		return self.rude_words
