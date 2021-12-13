from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import *


class AllProductListView(ListView):
    models = Product
    template_name = "store/home.html"

    def get_queryset(self):
        return Product.products.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/products/single.html"

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get("slug")
        return Product.object.filter(slug=slug).filter(in_stock=True)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.object.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "store/products/category.html", context=context)
