from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/products_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'
