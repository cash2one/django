from django.shortcuts import render,render_to_response
from db.models import Pyresult
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from echarts import Echart, Legend, Bar, Axis

def finalresult(request):
    limit = 3  # 每页显示的记录数
    topics = Pyresult.objects.all()
    paginator = Paginator(topics, limit)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    try:
        topics = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        topics = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render_to_response('finalresult.html', {'topics': topics})
# Create your views here.
