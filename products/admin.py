from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'employee')
  list_display_links = ('id', 'title')
  list_filter = ('employee',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description')
  list_per_page = 25

admin.site.register(Product, ProductAdmin)