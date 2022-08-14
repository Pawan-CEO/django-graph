from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Exams
from exam.utils import get_plot
# Create your views here.
def first(req):
    res=render(req,'exam\index.html')
    return res


def home(req):
    a=Exams.objects.all()
    x=[x.ename for x in a]
    y=[y.esal for y in a]
    chart=get_plot(x,y)
    print(chart)
    res=render(req,'exam/index.html',{'chart':chart})
    return res

