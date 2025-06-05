# generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_numbers, name='generate_numbers'),
    path('stats/', views.stats, name='stats'),
]