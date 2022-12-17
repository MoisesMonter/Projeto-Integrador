from django.shortcuts import render
from django.http import HttpResponse
'''from .models import Question'''
import datetime
# Create your views here.

def home(request):
    return render(request,'home.html')


def about_us(request):
    return render(request,'about_us.html')

def lista_de_eleicoes(request):
    return render(request,'lista_eleicoes.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def suport(request):
    return render(request,'suport_site.html')