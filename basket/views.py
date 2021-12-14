from django.shortcuts import render


def basket_summary(request):
    template_name = 'store/basket/summary.html'
    return render(request, template_name)
