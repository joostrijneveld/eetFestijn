from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Naam', max_length=200)
    wiebetaaltwat = forms.BooleanField(
        label='Betaalt via Wiebetaaltwat.nl',
        required=False)
