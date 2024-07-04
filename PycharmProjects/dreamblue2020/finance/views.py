from django.shortcuts import render

def property_list(request):
    return render(request, 'finance/property-list.html')

def property_detail(request, property_slug):
    # Fetching the correct property
    return render(request, 'finance/property-detail.html')