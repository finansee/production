from django.contrib import admin
from django.urls import path
from general import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-coaches/', views.findacoach, name='findacoach'),
    path('become-a-coach/', views.becomeacoach, name='becomeacoach'),
]
