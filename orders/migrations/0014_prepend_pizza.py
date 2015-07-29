# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_pizza(apps, schema_editor):
    Category = apps.get_model("orders", "Category")
    pizzas = Category.objects.get(name="Pizza's")
    for pizza in pizzas.items.all():
        if "Pizza" not in pizza.name and pizza.name[0] != "-":
            pizza.name = "Pizza " + pizza.name
            pizza.save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_randomsnacks'),
    ]

    operations = [
        migrations.RunPython(add_pizza)
    ]
