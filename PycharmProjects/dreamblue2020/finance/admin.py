from django.contrib import admin
from finance.models import Property, LeaseSpace, Expense, Tenant, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Categories', {
            'fields': ('name', 'property',)
        }),
    )

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fieldsets = (
                ('Location Information', {
                    'fields': ('name', 'budget', 'note'),
                }),
                # ('Tenants and Lease', {
                #     'fields': ('tenant', 'lease_space'),
                # }),
                # ('Expenses', {
                #     'fields': ('expense',),
                # }),
            )
#     lists_filter = ('name',)
#     list_display = ('name',)
#     fieldsets = (
#         ('Location Information', {
#              'fields': ('name',
#                         ('address_line_one', 'address_line_two'),
#                         ('city', 'zip_code'))
#          }),
#         ('Mortgage Information', {
#              'fields': (('mortgage_start_date', 'mortgage_end_date'),
#                         ('mortgage', 'mortgage_payment')),
#         }),
#         ('Tenants and Lease', {
#             'fields': ('tenant', 'lease_space'),
#         }),
#         ('Expenses', {
#             'fields': ('expense',),
#         }),
#     )


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    fieldsets = (
        ('None', {
            'fields': ('name', 'amount', 'property', 'category')

        }),
         )

@admin.register(LeaseSpace)
class LeaseSpaceAdmin(admin.ModelAdmin):

    fieldsets = (
        ('None', {
             'fields': ('name',)
                        }),
         )

@admin.register(Tenant)
class Tenant(admin.ModelAdmin):

    fieldsets = (
        ('None', {
             'fields':  (('last_name', 'first_name'),
                        ('email', 'telephone'),
                        ('note'),
                         ('start_date', 'end_date'),
                         ('rent')),
                        }),
         )
