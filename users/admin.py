#coding=utf-8
from django.contrib import admin

# Register your models here.

from .models import UserProfile#注册至admin
class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile,UserProfileAdmin)

