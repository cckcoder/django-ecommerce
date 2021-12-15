from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from .basket import Basket
from store.models import Product


def basket_summary(request):
    template_name = "store/basket/summary.html"
    return render(request, template_name)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = basket.__len__()

        return JsonResponse({"product_qty": basket_qty})
