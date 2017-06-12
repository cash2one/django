#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from programme.models import Search

class UserAsk(models.Model):
    name = models.CharField(max_length=10,verbose_name=u"姓名")
    mobile = models.CharField(max_length=11,verbose_name=u"手机")
    add_time = models.DateField(default=datetime.now,verbose_name=u"添加时间")
    history = models.ForeignKey(Search,verbose_name=u"查询记录")
    #外键，键入的programme中的值
    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


# Create your models here.
