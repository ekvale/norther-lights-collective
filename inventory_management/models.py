from django.db import models

# Create your models here.
# models.py
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    order_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    product_number = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=6, unique=True)
    raw_materials = models.ManyToManyField(RawMaterial, through='PurchaseOrderDetail')
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.po_number


class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity_ordered = models.FloatField()
    quantity_received = models.FloatField(null=True, blank=True)
    received_date = models.DateField(null=True, blank=True)


class FinishedProduct(models.Model):
    product_number = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    case_quantity = models.IntegerField()

    def __str__(self):
        return self.name


class KitchenBatch(models.Model):
    batch_number = models.CharField(max_length=4, unique=True)
    product = models.ForeignKey(FinishedProduct, on_delete=models.CASCADE)
    quantity_produced = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - Batch {self.batch_number}"


class QASpecification(models.Model):
    product_number = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    po_number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    specification = models.TextField()
    test_result = models.CharField(max_length=255, blank=True)
    passed = models.BooleanField(default=False)


class InventoryAdjustment(models.Model):
    product = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    adjustment_date = models.DateField(auto_now_add=True)
    quantity_adjusted = models.FloatField()
    reason = models.TextField()


class KitchenWorkOrder(models.Model):
    order_number = models.CharField(max_length=6, unique=True)
    raw_materials = models.ManyToManyField(RawMaterial, through='KitchenWorkOrderDetail')
    instructions = models.TextField()


class KitchenWorkOrderDetail(models.Model):
    kitchen_work_order = models.ForeignKey(KitchenWorkOrder, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity_allocated = models.FloatField()


class ShippingOrder(models.Model):
    order_number = models.CharField(max_length=6, unique=True)
    finished_products = models.ManyToManyField(FinishedProduct, through='ShippingOrderDetail')
    ship_date = models.DateField()


class ShippingOrderDetail(models.Model):
    shipping_order = models.ForeignKey(ShippingOrder, on_delete=models.CASCADE)
    finished_product = models.ForeignKey(FinishedProduct, on_delete=models.CASCADE)
    quantity_shipped = models.FloatField()
