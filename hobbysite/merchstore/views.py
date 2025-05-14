from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from user_management.models import Profile


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/products_list.html'
    def get_context_data(self, **kwargs):
        ctx = super(ProductListView, self).get_context_data(**kwargs)

        owner = None
        if self.request.user.is_authenticated:
            owner = Profile.objects.get(user=self.request.user)
            ctx['user_products'] = Product.objects.filter(owner=owner)


        ctx['all_products'] = Product.objects.exclude(owner=owner)
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'
