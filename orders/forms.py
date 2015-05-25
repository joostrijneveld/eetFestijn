from django.forms import ModelForm
from orders.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'wiebetaaltwat']
        labels = {'name': 'Naam',
                  'wiebetaaltwat': 'Betaalt via Wiebetaaltwat.nl'}
