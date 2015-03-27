from django.shortcuts import render

from orders.models import Item
from orders.forms import OrderForm

def index(request):
    item_list = Item.objects.all()
    form = OrderForm()
    context = {'item_list': item_list, 'form': form}
    return render(request, 'orders/index.html', context)

def summary(request):
    return render(request, 'orders/summary.html', None)

def overview(request):
    return render(request, 'orders/overview.html', None)
