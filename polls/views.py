from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello, world. You are at the polls index')

def chucha(request):
    return HttpResponse('chucha xd')
# Create your views here.
