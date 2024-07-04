from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='index'),
    path('about/', views.about, name='about'),
]
