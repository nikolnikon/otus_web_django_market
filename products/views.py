from django.shortcuts import render
from django.views import generic

from products.models import Product


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product

