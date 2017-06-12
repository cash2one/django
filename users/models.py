#coding=utf-8
#设计表{1.需要用户的登陆，注册，忘记密码中使用2.是否要权限}
#继承了auth_user表,但是需要增加字段
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django import forms
from django.db import models

class UserProfile(AbstractUser):
    birthday = models.DateField(default=datetime.now,verbose_name=u"出生日期")
    gender = models.CharField(max_length=10,choices=(('male',u"男"),('female',u"女")),default="female",verbose_name=u"性别")
    #choice可以用于轮播图
    adress = models.CharField(max_length=50,verbose_name=u"地址")
    mobile = models.CharField(max_length=11,verbose_name=u"手机号码")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=150,verbose_name=u"头像")
    #image用法upload_to 上传图片
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        def __unicode__(self):
            return self.name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50,verbose_name=u"验证码")
    email = models.EmailField(max_length=100,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(('register',u"注册"),('forget',u"找回密码")),max_length=15,verbose_name=u"发送邮件")
    send_time = models.DateField(default=datetime.now,verbose_name=u"发送时间")
    class Meta:
        verbose_name = u"邮箱验证"
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=150,verbose_name=u"轮播图")
    url = models.URLField(max_length=200,verbose_name=u"地址")
    index = models.IntegerField(default=100,verbose_name=u"顺序")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name



class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    class Meta:
        verbose_name = u"登陆注册"
        verbose_name_plural = verbose_name

from django.contrib import admin










 # Create your models here.
