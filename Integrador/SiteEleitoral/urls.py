from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name='home'),
    path('home/',views.Home, name='home'),
    path('about_us/',views.About_us,name='about_us'),
    path('lista_eleicoes/',views.ListaEleicoes,name='lista_eleicoes'),
    path('participando/', views.participando, name='participando'),
    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('reactive/',views.Reactive,name='reactive'),
    path('suport_site/',views.Suport,name='suport'),
    path('configuração/',views.Config,name='config'),
    path('configurar_Cargo/',views.config_Cargo,name='config_Cargo'),
    path('alterarpassword/',views.configkey,name='configkey'),
    path('deletarconta/',views.configdel,name='configdel'),
    path('logout/',views.Logout,name='Logout'),
    path('gerarumaeleicao/',views.gerarumaeleicao, name='gerarumaeleicao'),
    path('Urna/', views.Urna, name='Urna'),
    path('Urna/Registrar_Voto/',views.votar,name='votar'),
]
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)