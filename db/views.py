#coding=utf-8
from django.shortcuts import render,render_to_response
from .models import Pyresult
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from echarts import Echart, Legend, Bar, Axis

# def link_db(request):
#     shuju = Pyresult.objects.all()
#     return render(request,"select.html",{"shuju":shuju})

# def getcanshu(request):
#     return render(request, 'select.html')

    #获得了参数

# debug模式下 三个参数均能传递 ，现在需要完成功能 ：1.并连查询  2.贺哥说的缓存


    # latest_programme = Q(diming = 'location')|Q(url____contains = 'text')|Q(url____contains = 'process')
    # jieguo = Pyresult.objects.filter(latest_programme)

    # jieguo = Pyresult.objects.filter(Q(diming = location),Q(title__contains = text),Q(title__contains = process))
    #逻辑问题  1.三个下拉框 如果其中有一个是空的  是不是 and 之后全是空的  所以需要判断 if else
@cache_page(60*5)
# 之前的get方法改为post
def target(request):
    try:
        location = request.POST['area']
        process = request.POST['programme']
        text = request.POST['textbox']
        page = request.POST['page']
        l = len(location)
        p = len(process)
        t = len(text)
    except:
        return render(request,"error.html",{
        "unknown":'你的操作产生了一个错误,很有可能是因为进行了注入式查询，请返回上一页重新操作',

        })


#以下这段代码会使性能变的很卡，因为判断之后，每次都运行一次数据库，应该改为str类型的，最后写到fitler中
# 2017.6.2的思路：先不执行select操作，用字符串判断，最后写进
    if l != 0:
        q1 = Pyresult.objects.filter(diming = location).order_by("-shijian")
    else:
        q1 = Pyresult.objects.all().order_by("-shijian")
    if p != 0:
        q2 = q1.filter(title__contains = process).order_by("-shijian")
    else:
        q2 = q1
    if t != 0:
        q3 = q2.filter(title__contains = text).order_by("-shijian")
    else:
        q3 = q2

    jieguo = q3
    paginator = Paginator(jieguo, 15) # Show 10 contacts per page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    if len(jieguo) == 0:
        return render(request,"select.html",{
        "error":'该数据在数据库中不存在，请重新查询',
        "location":location,
        "process":process,
        "text":text,
        })
    else:
        # beijing = len(Pyresult.objects.filter(diming = "北京"))
        # tianjin = len(Pyresult.objects.filter(diming = "天津"))
        # shanghai = len(Pyresult.objects.filter(diming = "上海"))
        # chongqing = len(Pyresult.objects.filter(diming = "重庆"))
        # heilongjiang = len(Pyresult.objects.filter(diming = "黑龙江"))
        # jilin = len(Pyresult.objects.filter(diming = "吉林"))
        # liaoning = len(Pyresult.objects.filter(diming = "辽宁"))
        # hebei = len(Pyresult.objects.filter(diming = "河北"))
        # shanxi1 = len(Pyresult.objects.filter(diming = "山西"))
        # qinghai = len(Pyresult.objects.filter(diming = "青海"))
        # shandong = len(Pyresult.objects.filter(diming = "山东"))
        # henan = len(Pyresult.objects.filter(diming = "河南省"))
        # jiangsu = len(Pyresult.objects.filter(diming = "江苏"))
        # anhui = len(Pyresult.objects.filter(diming = "安徽"))
        # zhejiang = len(Pyresult.objects.filter(diming = "浙江"))
        # fujian = len(Pyresult.objects.filter(diming = "福建"))
        # jiangxi = len(Pyresult.objects.filter(diming = "江西"))
        # hunan = len(Pyresult.objects.filter(diming = "湖南"))
        # hubei = len(Pyresult.objects.filter(diming = "湖北"))
        # guangdong = len(Pyresult.objects.filter(diming = "广东"))
        # taiwan = len(Pyresult.objects.filter(diming = "台湾"))
        # hainan = len(Pyresult.objects.filter(diming = "海南"))
        # gansu = len(Pyresult.objects.filter(diming = "甘肃"))
        # shanxi = len(Pyresult.objects.filter(diming = "陕西"))
        # sichuan = len(Pyresult.objects.filter(diming = "四川省"))
        # guizhou = len(Pyresult.objects.filter(diming = "贵州"))
        # yunnan = len(Pyresult.objects.filter(diming = "云南"))
        # guangxi = len(Pyresult.objects.filter(diming = "广西"))
        # neimenggu = len(Pyresult.objects.filter(diming = "内蒙古"))
        # xizang = len(Pyresult.objects.filter(diming = "西藏"))
        # ningxia = len(Pyresult.objects.filter(diming = "宁夏"))
        # xinjiang = len(Pyresult.objects.filter(diming = "新疆"))


        return render(request,"select.html",{      #为了看echarts文件
            # "topics":topics,
            # "allinfo":allinfo,
        # "beijing":beijing,
        # "tianjin":tianjin,
        # "shanghai":shanghai,
        # "chongqing":chongqing,
        # "heilongjiang":heilongjiang,
        # "jilin":jilin,
        # "liaoning":liaoning,
        # "hebei":hebei,
        # "shanxi1" :shanxi1,
        # "qinghai" :qinghai,
        # "shandong" :shandong,
        # "henan":henan,
        # "jiangsu" :jiangsu,
        # "anhui" :anhui,
        # "zhejiang" :zhejiang,
        # "fujian":fujian,
        # "jiangxi":jiangxi,
        # "hunan":hunan,
        # "hubei" :hubei,
        # "guangdong" :guangdong,
        # "taiwan" :taiwan,
        # "hainan" :hainan,
        # "gansu":gansu,
        # "shanxi" :shanxi,
        # "sichuan" :sichuan,
        # "guizhou" :guizhou,
        # "yunnan" :yunnan,
        # "guangxi" :guangxi,
        # "neimenggu" :neimenggu,
        # "xizang" :xizang,
        # "ningxia" :ningxia,
        # "xinjiang":xinjiang,
        "location":location,
        "process":process,
        "text":text,
        "contacts":contacts
        })




    # if len(location) == len(process) == len(text) == 0:
    #     jieguo = Pyresult.objects.all()
    #     return render(request,"select.html",{"jieguo":jieguo})
    # elif len(location) == len(process) == 0 and len(text) != 0:
    #     jieguo = Pyresult.objects.filter(Q(title__contains = text))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    # elif len(location) == 0 and len(process) ==  len(text) != 0:
    #     jieguo = Pyresult.objects.filter(Q(title__contains = text),Q(title__contains = process))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    # elif len(location)  == 0 and len(process) != 0 and len(text) == 0:
    #     jieguo = Pyresult.objects.filter(Q(title__contains = process))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    # elif len(location) == len(process) == len(text) !=0:
    #     jieguo = Pyresult.objects.filter(Q(diming = location),Q(title__contains = process),Q(title__contains = text))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    # elif len(location) ==  len(process) != 0 and len(text) == 0:
    #     jieguo = Pyresult.objects.filter(Q(diming = location),Q(title__contains = process))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    #
    # elif len(location) == 0 and len(process) == len(text) != 0:
    #     jieguo = Pyresult.objects.filter(Q(title__contains = process),Q(title__contains = text))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})
    #
    #
    # else:
    #     # len(location) ==  0 and len(text) != 0 and len(process) ==0:
    #     jieguo = Pyresult.objects.filter(Q(diming = location),Q(title__contains = text))
    #     if len(jieguo) == 0:
    #         return render(request,"select.html",{"error":"抱歉~查询的数据数据库中不存在"})
    #     elif len(jieguo) != 0:
    #         return render(request,"select.html",{"jieguo":jieguo})

def firstvisit(request):
    return render(request, 'login.html')





















# Create your views here.
