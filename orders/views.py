from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from orders.models import Item, Order, ItemOrder
from orders.forms import OrderForm

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.name = form.cleaned_data['name']
            order.in_wie_betaalt_wat = form.cleaned_data['wiebetaaltwat']
            order.save()  # need to save to get an id, to prevent ValueError
            item_ids = request.POST.getlist('items[]')
            for item_id in item_ids:
                item = Item.objects.get(pk=item_id)
                order_item = ItemOrder.objects.create(item=item, order=order)
            order.save()
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
