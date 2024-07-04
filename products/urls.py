from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='product_search'),
]