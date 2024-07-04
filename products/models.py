from django.db import models
from datetime import datetime
from employees.models import Employee


# Create your models here.
class Product(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    count = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

