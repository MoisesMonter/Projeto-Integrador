from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home,name='home'),
    path('about_us',views.about_us,name='about_us'),
    path('lista_eleicoes',views.lista_de_eleicoes,name='lista_eleicoes'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('suport_site',views.suport,name='suport')
]