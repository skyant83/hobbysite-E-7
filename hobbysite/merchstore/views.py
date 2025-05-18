from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from user_management.models import Profile
from .models import Product, Transaction
from .forms import TransactionForm, ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/product_list.html'

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
                current_profile = Profile.objects.get(user=self.request.user)
                transaction.buyer = current_profile
                transaction.product = self.get_object()
                transaction.status = 'OC'
                product = self.get_object()
                updated_stock = product.stock - transaction.amount
                if updated_stock <= 0:
                    updated_stock = 0
                    transaction.amount = product.stock
                    product.status = 'OOS'
                product.stock = updated_stock
                product.save()
                transaction.save()
                return redirect('merchstore:cart_list')
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
            form = TransactionForm(
                initial={'amount': request.session['transaction_amount']})
            context['transaction_form'] = form
            return self.render_to_response(context)
        return self.render_to_response(context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'merchstore/product_edit.html'

    def form_valid(self, form):
        if form.instance.stock <= 0:
            form.instance.stock = 0
            form.instance.status = 'OOS'
        else:
            form.instance.status = 'AV'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:product_detail',
                            kwargs={'pk': self.kwargs['pk']})


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'merchstore/product_create.html'

    def form_valid(self, form):
        form.instance.owner = Profile.objects.get(user=self.request.user)
        if form.instance.stock <= 0:
            form.instance.stock = 0
            form.instance.status = 'OOS'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('merchstore:product_detail',
                            kwargs={'pk': self.object.pk})


class CartView(ListView):
    model = Product
    template_name = 'merchstore/cart.html'

    def get_context_data(self, **kwargs):
        ctx = super(CartView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            owner = Profile.objects.get(user=self.request.user)
            ctx['product_cart'] = Transaction.objects.filter(buyer=owner)
        return ctx


class TransactionListView(ListView):
    model = Product
    template_name = 'merchstore/transaction_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(TransactionListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_profile = Profile.objects.get(user=self.request.user)
            ctx['sold_transactions'] = \
                Transaction.objects.filter(product__owner=current_profile)
        return ctx
