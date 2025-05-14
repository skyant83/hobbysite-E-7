from django.contrib import admin
from .models import Product, ProductType, Transaction


class TransactionInline(admin.StackedInline):
    model = Transaction


class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [TransactionInline]


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
