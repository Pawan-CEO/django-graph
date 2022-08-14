from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first2(req):
    a='<h3>first exam2 screen</h3>'
    return HttpResponse(a)