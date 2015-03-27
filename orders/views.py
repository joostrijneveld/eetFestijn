from django.shortcuts import render

from orders.models import Item

def index(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'orders/index.html', context)

def summary(request):
    return render(request, 'orders/summary.html', None)

def overview(request):
    return render(request, 'orders/overview.html', None)
