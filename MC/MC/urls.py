

from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from mciklimlendirme import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('tr/dokumanlar/', views.dokumanlar, name='dokumanlar'),
    path('tr/esanjor/', views.esanjor, name='esanjor'),
    path('tr/teklifal/', views.teklifal, name='teklifal'),
    path('tr/hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('tr/gizlilik-politikasi/', views.gp, name='gizlilikpolitikasi'),
    path('', RedirectView.as_view(url='/tr', permanent=True)),
    path('tr/', views.index, name='index'),
    path('form-submit/', views.process_form, name='process_form'),
    path('tr/esanjor2/', views.esanjor2, name='esanjor2'),
    path('en/documents/', views.dokumanlar2, name='dokumanlar2'),
    path('en/exchanger/', views.esanjoren, name='esanjoren'),
    path('en/exchanger2/', views.esanjoren2, name='esanjoren2'),
    path('en/about-us/', views.hakkimizda2, name='hakkimizda2'),
    path('en/privacypolicy/', views.gp2, name='gp2'),
    path('en/', views.index2, name='index2'),
    path('iletisim-form', views.contact_form, name='contact_form'),
    path('en/quote', views.teklifal2, name='teklifal2')
    
  
    
]


