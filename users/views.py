#coding=utf-8
#登陆逻辑
from django.shortcuts import render
from django.contrib.auth import authenticate#用户名，密码验证
from django.contrib.auth import login
from django.views.generic.base import View
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from .models import UserForm
from .models import UserProfile
import time
import image

# class LoginView(View):
#     def get(self,request):
#         return render(request,"login.html", {})
#     def post(self,request):
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():#是否为空
#             user_name = request.POST.get("username","")
#             pass_word = request.POST.get("password","")
#             user = authenticate(username = user_name,password =pass_word)#验证，失败的话返回空值
#             if user is not None:
#                 login(request,user)
#                 return render(request,"guest_center.html",)
#             else:
#                 return render(request,"login.html",{"message":"用户名或密码出错"})
#         else:
#             return render(request,"login.html",{"login_form":"login_form"})
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名',max_length=50)
#     password = forms.CharField(label='密码',widget=forms.PasswordInput())
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True,min_length=1)
def user_login(request):
    if request.method == "POST":
        user_name =request.POST.get("username","")
        pass_word =request.POST.get("password","")
        mobile_phone = request.POST.get("mobile","")
        # user = authenticate(username = user_name,password =pass_word)#验证，失败的话返回空值
        logininfo = UserProfile(request.POST)
        comperawith = UserProfile.objects.filter(username__exact = user_name , password__exact= pass_word)
        if comperawith:
            # login(request,logininfo)
            time.sleep(1.5)
            return render(request,"select.html",{})#传参为空
        else:
            time.sleep(1.5)
            return render(request,"login.html",{"message":"用户名或密码错误"})
    elif request.method == "GET":
        return render(request,"login.html", {})
        # if user is not None:
        #     login(request,user)
    #         return render(request,"guest_center.html",{})#传参为空
    #     else:
    #         return render(request,"login.html",{"message":"用户名或密码错误"})
    # elif request.method == "GET":
    #     return render(request,"login.html", {})


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=1)
def user_register(request):
    if request.method == "POST":
        user_name =request.POST.get("username","")
        pass_word =request.POST.get("password","")
        userregister = RegisterForm(request.POST)
        if userregister.is_valid():
            username = userregister.cleaned_data['username']
            password = userregister.cleaned_data['password']
            filterResult =UserProfile.objects.filter(username = username)
            if len(filterResult)>0:
                return render_to_response('register.html',{'errorr':"用户名已存在，请更换"})
            else:
                user = UserProfile.objects.create(username=username,password=password)
                # UserProfile.save()
                return render(request,"register.html",{"info":"注册成功，请于登陆页面进行登录"})
    else:
        return render(request,"register.html")




#
#
# class RegisterView(View):
#     def get(self,request):
#         register_form = RegisterForm()
#         return render(request,"register.html",{"register_form":register_form})
#     def post(self,request):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             pass

# http://www.cnblogs.com/Mr-wanwan/p/6439116.html
# def regist(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#             UserRe.objects.create(username=username,password=password)
#             UserRe.save()
#             return HttpResponse('regist success!!!')
#         else:
#             userform = UserForm()
#         return render_to_response('regist.html',{'userform':userform})
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名',max_length=50)
#     password = forms.CharField(label='密码',widget=forms.PasswordInput())
# def regist(request):
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#             UserForm.objects.create(username=username,password=password,)
#             UserForm.save()
#             return render(request,"login.html",{"message":"注册成功"})
#     else:
#         userform = UserForm()
#         return render(request,"register.html",{"userform":userform})
#
#
# def login(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#
#             user = UserForm.objects.filter(username__exact=username,password__exact=password)
#
#             if user:
#                 return render_to_response('index.html',{'userform':userform})
#             else:
#                 return HttpResponse('用户名或密码错误,请重新登录')
#
#     else:
#         userform = UserForm()
#     return render_to_response('login.html',{'userform':userform})

# Create your views here.
