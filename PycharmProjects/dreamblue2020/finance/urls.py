from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.property_list, name='list'),
    path('<slug:property_slug>', views.property_detail, name='detail')
]
