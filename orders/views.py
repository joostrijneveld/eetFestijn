from django.http import HttpResponse
from django.template import RequestContext, loader

from orders.models import Item

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('orders/index.html')
    context = RequestContext(request, {
        'item_list': item_list,
    })
    return HttpResponse(template.render(context))
