from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from product.forms import ProductForm
from product.models import Product


class ProductCreatView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'product/product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('homepage')
    permission_required = 'product.add_product'


class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "product/update_product.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_of_products')
    permission_required = 'product.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list_of_products')
    permission_required = 'product.delete_product'


class ProductDetailsView(DetailView):
    template_name = 'product/detail_product.html'
    model = Product
