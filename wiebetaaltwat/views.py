from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError

from .models import Participant
from orders.models import Order

import requests


def update_lists(request):
    if Order.objects.count() > 0:
        return HttpResponseServerError(
            "Cowardly refusing to update the list while there are orders."
        )
    session, response = _create_wbw_session()
    url = ('https://api.wiebetaaltwat.nl/api/lists/{list_id}/members'
           .format(list_id=settings.WBW_LIST_ID))
    response = session.get(url,
                           headers={'Accept-Version': '1'},
                           cookies=response.cookies)
    data = response.json()
    Participant.objects.all().delete()
    for item in data['data']:
        uid = item['member']['id']
        if uid == settings.WBW_UID:
            continue
        name = item['member']['nickname']
        participant, _ = Participant.objects.get_or_create(wbw_id=uid)
        participant.name = name
        participant.save()
    return HttpResponse("Participants updated!")


def _create_wbw_session():
    session = requests.Session()
    payload = {'user': {
        'email': settings.WBW_EMAIL,
        'password': settings.WBW_PASSWORD,
        }
    }
    response = session.post('https://api.wiebetaaltwat.nl/api/users/sign_in',
                            json=payload,
                            headers={'Accept-Version': '1'})
    return session, response
