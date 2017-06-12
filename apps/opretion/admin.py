#coding=utf-8
from django.contrib import admin

# Register your models here.

from .models import UserAsk
class UserAskAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserAsk,UserAskAdmin)
# Register your models here.
