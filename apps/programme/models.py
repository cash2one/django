#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from users.models import UserProfile

class Search(models.Model):
    name = models.ForeignKey(UserProfile,verbose_name=u"查询人")
    history = models.CharField(max_length=100,verbose_name=u"查询记录")
    time = models.DateField(default=datetime.now,verbose_name=u"查询时间")
    class Meta:
        verbose_name = u"查询操作"
        verbose_name_plural = verbose_name
# Create your models here.
