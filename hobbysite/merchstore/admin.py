from django.contrib import admin
from .models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
