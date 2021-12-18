from django.http import request
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


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        basket.delete(product_id=product_id)
        basket_qty = basket.__len__()
        basket_total_price = basket.get_total_price()

        resp = JsonResponse(
            {"basket_qty": basket_qty, "sub_total_price": basket_total_price}
        )
        return resp


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        basket.update(product_id=product_id, product_qty=product_qty)

        basket_qty = basket.__len__()
        basket_total_price = basket.get_total_price()

        resp = JsonResponse(
            {"basket_qty": basket_qty, "sub_total_price": basket_total_price}
        )
        return resp
