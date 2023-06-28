from django.contrib import admin
from django.urls import path
from main.views import index, about, product, productdetails, a, b, c

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('product/<int:pk>', productdetails, name='pd_detail'),
    path('a/', a, name='a'),
    path('b/', b, name='b'),
    path('c/', c, name='c'),
]