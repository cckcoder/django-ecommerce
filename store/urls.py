from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.AllProductListView.as_view(), name="product_all"),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
]
