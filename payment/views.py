import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price()).replace(".", "")
    total = int(total)
    stripe.api_key = "pk_test_51Ih3abLrydoSDKK6mZ8NDQz3pIv8kFqN4mgtZsUW1kDdY7UkQzZSaeP5KmAeVxDYSayNuRubUfQU0x7mJFq4Gyfs00jacy1Y4R"

    intent = stripe.PaymentIntent.create(
        amount=total, currency="gbp", metadata={"userid": request.user.id}
    )
    template = "payment/home.html"
    return render(request, template)
