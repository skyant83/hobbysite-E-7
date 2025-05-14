from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse

from user_management.models import Profile
from .models import Product, TRANSACTION_STATUS, PRODUCT_STATUS
from .forms import TransactionForm


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/products_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['transaction_form'] = TransactionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                transaction = form.save(commit=False)
                current_profile = Profile.objects.get(user=request.user)
                transaction.buyer = current_profile
                transaction.product = self.get_object()
                transaction.status = 'OC'
                product = self.get_object()
                updated_stock = product.stock - transaction.amount
                if updated_stock <= 0:
                    updated_stock = 0
                    product.status = 'OOS'
                product.stock = updated_stock
                product.save()
                transaction.save()
                return redirect('merchstore:cart_list', pk=self.kwargs['pk'])
            else:
                request.session['transaction_amount'] = \
                    form.cleaned_data['amount']
                return redirect(reverse('accounts:login')+'?next='+request.path)
        else:
            self.object = self.get_object()
            context = self.get_context_data(**kwargs)
            context['transaction_form'] = form
            return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'transaction_amount' in request.session:
            context['transaction_form'] = \
                TransactionForm(amount=request.session['transaction_amount'])
            return self.render_to_response(context)
        return self.render_to_response(context)
