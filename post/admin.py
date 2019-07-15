from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Comment, Category, Message
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Message)
admin.site.unregister(User)
admin.site.unregister(Group)