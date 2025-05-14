from django.contrib import admin
from .models import Product, ProductType, Transaction


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    search_fields = ('buyer', 'product', 'status')
    list_display = ('buyer', 'product', 'amount', 'status', 'created_on')
    list_filter = ('buyer', 'product', 'amount', 'status', 'created_on')
    fieldsets = (
        ('Transaction Details', {
            'fields': (
                ('buyer', 'product'),
                ('amount', 'status',)
            ),
        }),
    )


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', 'status')
    list_display = ('name', 'product_type', 'owner', 'description', 'price', 'stock', 'status')
    list_filter = ('name', 'product_type', 'owner', 'description', 'price', 'stock', 'status')
    fieldsets = (
        ('Product Details', {
            'fields': (
                ('name', 'owner'),
                ('product_type', 'price', 'stock', 'status'),
                ('description'),
            ),
        }),
    )


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)
    fieldsets = (
        ('Product Type Details', {
            'fields': (
                ('name'),
                ('description')
            ),
        }),
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)