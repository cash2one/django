#coding=utf-8
from django.contrib import admin

# Register your models here.

from .models import Search
class SearchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Search,SearchAdmin)
# Register your models here.