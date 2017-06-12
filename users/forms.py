#coding=utf-8
__author__ = 'thinkpad'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=1)

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=1)