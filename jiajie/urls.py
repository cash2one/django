#coding=utf-8
"""jiajie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from users.views import user_login
# from db.views import link_db
# from db.views import getcanshu
from db.views import target
from users.views import user_register
# from fenye.views import finalresult
from db.views import firstvisit
urlpatterns = [
    url(r'^$', firstvisit , name="firstvisit"),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',  user_login  , name="login"),
    url(r'^register/$', user_register ,name="register"),
    url(r'^guest_center/', TemplateView.as_view(template_name="guest_center.html"),name="guest_center"),
    # url(r'^result/$', getcanshu , name="getcanshu"),
    url(r'^select/$', target , name="target"),


    # url(r'^finalresult/$', finalresult , name="finalresult"),0




]
