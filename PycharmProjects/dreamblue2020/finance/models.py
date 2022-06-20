from django.db import models
from phone_field import PhoneField
from django.utils.text import slugify


class Tenant(models.Model):

    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    email = models.EmailField()
    telephone = PhoneField(blank=True, help_text='Contact Phone Number')
    note = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()
    rent = models.IntegerField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class LeaseSpace(models.Model):
    name = models.CharField(max_length=128)
    address_line_one = models.CharField(max_length=128)
    address_line_two = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=128)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):

    class Meta:
        verbose_name_plural = u'Properties'

    slug = models.SlugField(max_length=100, unique=True, blank=True)
    # Address
    name = models.CharField(max_length=128)
    budget = models.IntegerField()
    note = models.TextField(blank=True, default='')
    # address_line_one = models.CharField(max_length=128)
    # address_line_two = models.CharField(max_length=128, blank=True)
    # zip_code = models.CharField(max_length=12)
    # city = models.CharField(max_length=128)
    #
    # # Mortgage
    # mortgage_start_date = models.DateField()
    # mortgage_end_date = models.DateField()
    # mortgage = models.IntegerField()
    # mortgage_payment = models.IntegerField()

    # # Tenants
    # tenant = models.ManyToManyField(Tenant, related_name="tenants")
    #
    # # Lease Spaces
    # lease_space = models.ManyToManyField(LeaseSpace, related_name="lease_spaces")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)


class Category(models.Model):

    class Meta:
        verbose_name_plural = u'Categories'

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
