from collections import Counter

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
            messages.success(request, "Bestelling succesvol doorgegeven!")
            return HttpResponseRedirect(reverse('orders:index'))
    else:
        form = OrderForm()
    context = {'item_list': Item.objects.all(), 'form': form}
    return render(request, 'orders/index.html', context)

def summary(request):
    c = Counter()
    for order in Order.objects.all():
        for item in order.items.all():
            c.update([item.name])
    context = {'combined_order': dict(c)}
    return render(request, 'orders/summary.html', context)

def overview(request):
    if request.method == 'POST' and request.POST['remove']:
        if request.POST['remove'] == 'all':
            Order.objects.all().delete()
            messages.success(request, "Alle bestellingen verwijderd!")
        else:
            order = Order.objects.get(pk=request.POST['remove'])
            msg = "Bestelling van {.name} verwijderd!".format(order)
            order.delete()
            messages.success(request, msg)
        return HttpResponseRedirect(reverse('orders:overview'))

    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders/overview.html', context)
