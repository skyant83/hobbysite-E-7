from django import forms

from .models import Transaction, Product, PRODUCT_STATUS, TRANSACTION_STATUS


class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ['amount']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'product_type',
                  'description',
                  'price',
                  'stock',
                  'status']
        widgets = {
            'product_type': forms.Select,
            'status': forms.Select(choices=PRODUCT_STATUS)
        }