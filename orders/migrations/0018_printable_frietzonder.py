# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def printable_frietzonder(apps, schema_editor):
    Item = apps.get_model('orders', 'Item')
    frietzonder = Item.objects.get(name='personen friet')
    frietzonder.name = 'Friet zonder'
    frietzonder._printable_name = 'personen friet'
    frietzonder.save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_item__printable_name'),
    ]

    operations = [
        migrations.RunPython(printable_frietzonder)
    ]
