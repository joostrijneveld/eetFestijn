# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def fix_frietzonder(apps, schema_editor):
    Item = apps.get_model("orders", "Item")
    Category = apps.get_model("orders", "Category")
    friet = Category.objects.get(name="Friet of rasfriet")

    Item.objects.get(name="Friet zonder (klein)").delete()
    Item.objects.get(name="Friet zonder (groot)").delete()
    zonder = Item.objects.create(name="personen friet", price=160)
    friet.items.add(zonder.pk)


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_festcategories'),
    ]

    operations = [
        migrations.RunPython(fix_frietzonder)
    ]
