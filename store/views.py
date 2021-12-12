from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import *


def categories(request):
    return {"categories": Category.objects.all()}


class AllProductListView(ListView):
    models = Product
    template_name = "store/home.html"

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/products/item_detail.html"

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get("slug")
        return Product.objects.filter(slug=slug).filter(in_stock=True)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "store/products/category.html", context=context)
