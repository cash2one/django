from django.test import TestCase
from echarts import Echart, Legend, Bar, Axis
from .models import Pyresult
def link_db(request):
    shuju = Pyresult.objects.all()
    return
# Create your tests here.
