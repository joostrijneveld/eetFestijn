# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_chili(apps, schema_editor):
    Item = apps.get_model("orders", "Item")
    Category = apps.get_model("orders", "Category")

    sauzen = Category.objects.get(name="Sauzen")
    sauzen.items.add(Item.objects.create(name='Sweet Chili-saus', price=100))


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20160925_1609'),
    ]

    operations = [
        migrations.RunPython(add_chili)
    ]
