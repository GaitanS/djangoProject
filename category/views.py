from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.forms import CategoryForm
from category.models import Category


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list_of_categories')
    permission_required = 'category.add_category'


class CategoryListView(ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "category/update_category.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list_of_categories')
    permission_required = 'category.change_category'


# UPDATEVIEW() 1. VIEWS.PY- veti crea clasa CategoryUpdateView impreuna cu (template_name, model, form_class,
# success_url) 2. In templates veti crea fisierul html, unde veti avea formularul pentru a va actuliza informatiile
# despre categoria respectiva 3 in URLS.PY veti defini url pentru clasa creata din views.py.

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list_of_categories')
    permission_required = 'category.delete_category'


@login_required()
@permission_required('category.delete_category_by_popup')
def delete_category_with_popup(request, pk):
    current_category = Category.objects.filter(id=pk)
    current_category.delete()
    return redirect('list_of_categories')


class CategoryDetailsView(DetailView):
    template_name = 'category/detail_category.html'
    model = Category
