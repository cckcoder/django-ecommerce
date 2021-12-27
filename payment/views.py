import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    for b in basket:
        print(b)

    total = str(basket.get_total_price()).replace(".", "")
    total = int(total)
    template = "payment/home.html"
    return render(request, template)
