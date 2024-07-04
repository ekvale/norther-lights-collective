from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Product

def index(request):
    products = Product.objects.order_by('-created_at').filter(is_published=True)

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)

def search(request):
    queryset_list = Product.objects.order_by('-created_at')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'products': queryset_list,
        'values': request.GET
    }

    return render(request, 'products/search.html', context)
