from django.shortcuts import render
from django.http import HttpResponse
#from .models import Question
import datetime
# Create your views here.

def home(request):
    x= int(1)
    return render(request,'home.html',{'x': x})


def about_us(request):
    x= int(1)
    return render(request,'about_us.html',{'x': x})

def lista_de_eleicoes(request):
    x= int(1)
    return render(request,'lista_eleicoes.html',{'x': x})

def login(request):
    x= int(1)
    return render(request,'login.html',{'x': x})

def register(request):
    x= int(1)
    return render(request,'register.html',{'x': x})

def suport(request):
    x= int(1)
    return render(request,'suport_site.html',{'x': x})