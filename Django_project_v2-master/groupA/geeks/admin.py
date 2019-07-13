from django.contrib import admin
from .models import category, forbidden,Post,Comment,Reply

# Register your models here.
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(category)
admin.site.register(forbidden)
