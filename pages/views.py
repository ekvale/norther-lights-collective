from django.shortcuts import render
from products.models import Product
from employees.models import Employee

def index(request):
    products = Product.objects.order_by('-created_at').filter(is_published=True)

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)

def about(request):
    employees = Employee.objects.order_by('-hire_date')

    context = {
        'employees': employees,
    }

    return render(request, 'pages/about.html', context)

def alternate(request):
    return render(request, 'pages/alternate.html')

def landing(request):
    return render(request, 'pages/landing.html')