from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import (
    Supplier, RawMaterial, PurchaseOrder, PurchaseOrderDetail,
    FinishedProduct, KitchenBatch, QASpecification, InventoryAdjustment,
    KitchenWorkOrder, KitchenWorkOrderDetail, ShippingOrder, ShippingOrderDetail
)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_link')

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'name', 'supplier')

class PurchaseOrderDetailInline(admin.TabularInline):
    model = PurchaseOrderDetail

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'order_date')
    inlines = [PurchaseOrderDetailInline]

@admin.register(FinishedProduct)
class FinishedProductAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'name', 'case_quantity')

@admin.register(KitchenBatch)
class KitchenBatchAdmin(admin.ModelAdmin):
    list_display = ('batch_number', 'product', 'quantity_produced')

@admin.register(QASpecification)
class QASpecificationAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'po_number', 'specification', 'test_result', 'passed')

@admin.register(InventoryAdjustment)
class InventoryAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'adjustment_date', 'quantity_adjusted', 'reason')

class KitchenWorkOrderDetailInline(admin.TabularInline):
    model = KitchenWorkOrderDetail

@admin.register(KitchenWorkOrder)
class KitchenWorkOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'instructions')
    inlines = [KitchenWorkOrderDetailInline]

class ShippingOrderDetailInline(admin.TabularInline):
    model = ShippingOrderDetail

@admin.register(ShippingOrder)
class ShippingOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'ship_date')
    inlines = [ShippingOrderDetailInline]
