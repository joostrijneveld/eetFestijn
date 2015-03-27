from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from orders.models import Item
from orders.forms import OrderForm

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('orders:success'))
    else:
        form = OrderForm()
    context = {'item_list': Item.objects.all(), 'form': form}
    return render(request, 'orders/index.html', context)

def success(request):
    messages.success(request, "Bestelling succesvol doorgegeven!")
    return index(request)

def summary(request):
    return render(request, 'orders/summary.html', None)

def overview(request):
    return render(request, 'orders/overview.html', None)
