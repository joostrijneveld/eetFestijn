from collections import Counter
import json
from six.moves import urllib

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.conf import settings
from django.forms.models import model_to_dict

from orders.models import Item, Order, ItemOrder, Category, Receipt
from orders.forms import OrderForm
from orders.templatetags.display_euro import euro

import weasyprint
import dateutil.parser
from orders.utils import DateTimeEncoder


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            item_ids = request.POST.getlist('items[]')
            for item_id in item_ids:
                item = Item.objects.get(pk=item_id)
                ItemOrder.objects.create(item=item, order=order)
            messages.success(request, "Bestelling succesvol doorgegeven!")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = OrderForm()
    categories = Category.objects.all().prefetch_related('items__discounts')
    total = Item.objects.count()
    n = 0
    cols = [[], []]
    for category in categories:
        cols[0 if n < total/2 else 1].append(category)
        n += category.items.count()
    context = {'cols': cols, 'form': form}
    return render(request, 'orders/index.html', context)


def summary(request):
    c = Counter()
    for order in Order.objects.all():
        for item in order.items.all():
            c.update([item.printable_name])
    context = {'combined_order': sorted(dict(c).items())}
    return render(request, 'orders/summary.html', context)


def summary_PDF(request):
    html = summary(request).content
    response = HttpResponse(content_type="application/pdf")
    base_url = request.build_absolute_uri()
    weasyprint.HTML(string=html, base_url=base_url).write_pdf(response)
    return response


def receipts(request):
    receipts = Receipt.objects.order_by('-date')
    for receipt in receipts:
        receipt.dict = json.loads(receipt.contents)
        if receipt.dict['orders'] and 'date' in receipt.dict['orders'][0]:
            for order in receipt.dict['orders']:
                    order['date'] = dateutil.parser.parse(order['date'])
            receipt.latest = min(x['date'] for x in receipt.dict['orders'])
    return render(request, 'orders/receipts.html', {'receipts': receipts})


def overview(request):
    if request.method == 'POST':
        if 'process' in request.POST:
            orders = []
            for order in Order.objects.all():
                orderdict = model_to_dict(order)
                orderdict['items'] = [{'name': item.name,
                                       'price': item.real_price(order.date)}
                                      for item in order.items.all()]
                orderdict['total'] = order.total()
                orders.append(orderdict)
            if orders:
                receipt = {'grandtotal': Order.grandtotal(),
                           'orders': orders}
                contents = json.dumps(receipt, cls=DateTimeEncoder)
                Receipt(contents=contents).save()
                Order.objects.all().delete()
            messages.success(request, "Alle bestellingen verwerkt!")
        elif 'remove' in request.POST:
            order = Order.objects.get(pk=request.POST['remove'])
            msg = "Bestelling van {.name} verwijderd!".format(order)
            order.delete()
            messages.success(request, msg)
        elif 'slack' in request.POST and hasattr(settings, 'SLACK'):
            jsondata = {'text': 'Nieuwe bestelling!',
                        'channel': settings.SLACK['channel'],
                        'username': settings.SLACK['username'],
                        'icon_emoji': settings.SLACK['icon_emoji']}
            for order in Order.objects.all():
                jsondata['text'] += '\n*{}* ({}):'.format(
                    order.name, euro(order.total()))
                items = [' {} ({})'.format(item.name,
                                           euro(item.real_price(order.date)))
                         for item in order.items.all()]
                jsondata['text'] += ', '.join(items)
            payload = {'payload': json.dumps(jsondata)}
            data = urllib.parse.urlencode(payload).encode('UTF-8')
            req = urllib.request.Request(settings.SLACK['webhook'], data)
            urllib.request.urlopen(req)
            messages.success(request, "Bestellingen gedeeld via Slack!")
        return HttpResponseRedirect(reverse('overview'))

    orders = Order.objects.all()
    context = {'orders': orders, 'grandtotal': Order.grandtotal(),
               'slack': hasattr(settings, 'SLACK')}
    return render(request, 'orders/overview.html', context)
