from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError

from .models import Participant
from orders.models import Order

from bs4 import BeautifulSoup
import requests


def update_lists(request):
    if Order.objects.count() > 0:
        return HttpResponseServerError(
            "Cowardly refusing to update the list while there are orders."
        )
    session, response = _create_wbw_session()
    url = ('https://wiebetaaltwat.nl/index.php?lid={}&page=members'
           .format(settings.WBW_LIST_ID))
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trs = soup.tbody.findAll('tr')
    data = [(tr.attrs['id'][7:], next(tr.td.span.children)) for tr in trs]
    data = [(uid, name) for uid, name in data if uid != settings.WBW_UID]
    Participant.objects.all().delete()
    for uid, name in data:
        participant, _ = Participant.objects.get_or_create(wbw_id=uid)
        participant.name = name
        participant.save()
    return HttpResponse("Participants updated!")


def _create_wbw_session():
    session = requests.Session()
    payload = {'action': 'login', 'username': settings.WBW_EMAIL,
               'password': settings.WBW_PASSWORD, 'login_submit': 'Inloggen'}
    response = session.post('https://wiebetaaltwat.nl', payload)
    return (session, response)
