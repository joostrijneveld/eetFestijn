from collections import Counter
import json
import urllib

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings

from orders.models import Item, Order, ItemOrder
from orders.forms import OrderForm
from orders.templatetags.display_euro import euro

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.name = form.cleaned_data['name']
            order.wiebetaaltwat = form.cleaned_data['wiebetaaltwat']
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
    item_list = Item.objects.all()
    col1 = item_list[:(len(item_list)+1)//2]
    col2 = item_list[(len(item_list)+1)//2:]
    context = {'col1': col1, 'col2': col2, 'form': form}
    return render(request, 'orders/index.html', context)

def summary(request):
    c = Counter()
    for order in Order.objects.all():
        for item in order.items.all():
            c.update([item.name])
    context = {'combined_order': dict(c)}
    return render(request, 'orders/summary.html', context)

def overview(request):
    if request.method == 'POST':
        if 'remove' in request.POST:
            if request.POST['remove'] == 'all':
                Order.objects.all().delete()
                messages.success(request, "Alle bestellingen verwijderd!")
            else:
                order = Order.objects.get(pk=request.POST['remove'])
                msg = "Bestelling van {.name} verwijderd!".format(order)
                order.delete()
                messages.success(request, msg)
            return HttpResponseRedirect(reverse('orders:overview'))
        elif 'slack' in request.POST and hasattr(settings, 'SLACK'):
            jsondata = {'text' : 'Nieuwe bestelling!',
                        'channel' : settings.SLACK['channel'],
                        'username' : settings.SLACK['username'],
                        'icon_emoji' : settings.SLACK['icon_emoji']}
            for order in Order.objects.all():
                jsondata['text'] += '\n*{}* ({}):'.format(
                    order.name, euro(order.total()))
                items = [' {} ({})'.format(item.name, euro(item.real_price))
                    for item in order.items.all()]
                jsondata['text'] += ', '.join(items)
            payload = {'payload' : json.dumps(jsondata)}
            data = urllib.parse.urlencode(payload).encode('UTF-8')
            req = urllib.request.Request(settings.SLACK['webhook'], data)
            urllib.request.urlopen(req)
            messages.success(request, "Bestellingen gedeeld via Slack!")
            return HttpResponseRedirect(reverse('orders:overview'))

    orders = Order.objects.all()
    context = {'orders': orders, 'grandtotal': Order.grandtotal(),
        'slack': hasattr(settings, 'SLACK')}
    return render(request, 'orders/overview.html', context)
