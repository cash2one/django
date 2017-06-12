from django.shortcuts import render,render_to_response
from db.models import Pyresult
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from echarts import Echart, Legend, Bar, Axis

def finalresult(request):
    limit = 3  # ÿҳ��ʾ�ļ�¼��
    topics = Pyresult.objects.all()
    paginator = Paginator(topics, limit)  # ʵ����һ����ҳ����

    page = request.GET.get('page')  # ��ȡҳ��
    try:
        topics = paginator.page(page)  # ��ȡĳҳ��Ӧ�ļ�¼
    except PageNotAnInteger:  # ���ҳ�벻�Ǹ�����
        topics = paginator.page(1)  # ȡ��һҳ�ļ�¼
    except EmptyPage:  # ���ҳ��̫��û����Ӧ�ļ�¼
        topics = paginator.page(paginator.num_pages)  # ȡ���һҳ�ļ�¼

    return render_to_response('finalresult.html', {'topics': topics})
# Create your views here.
