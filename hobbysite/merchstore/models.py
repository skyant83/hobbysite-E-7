from django.db import models
from django.urls import reverse

from user_management.models import Profile

PRODUCT_STATUS = [
    'Available',
    'On sale',
    'Out of stock',
]

TRANSACTION_STATUS = [
    'On cart',
    'To Pay',
    'To Ship',
    'To Receive',
    'Delivered',
]


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_type'
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(default='Available', choices=PRODUCT_STATUS)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:product_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']


class Transaction(models.Model):
    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.IntegerField()
    status = models.CharField(choices=TRANSACTION_STATUS)
    created_on = models.DateTimeField(auto_now_add=True)
