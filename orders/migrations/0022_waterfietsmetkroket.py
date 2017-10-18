# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_waterfiets_kroket(apps, schema_editor):
    Item = apps.get_model("orders", "Item")
    Category = apps.get_model("orders", "Category")

    friet = Category.objects.get(name="Friet of rasfriet")
    friet.items.add(Item.objects.create(name='Friet waterfiets met kroketten (klein)', price=450))
    friet.items.add(Item.objects.create(name='Friet waterfiets met kroketten (groot)', price=500))


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_chillisaus'),
    ]

    operations = [
        migrations.RunPython(add_waterfiets_kroket)
    ]
