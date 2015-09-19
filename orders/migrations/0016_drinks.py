# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_drinks(apps, schema_editor):
    """This adds the drinks available at the Fest (but not listed on the menu)
    """

    Item = apps.get_model("orders", "Item")
    Category = apps.get_model("orders", "Category")

    drinks = Category.objects.create(name="Dranken")
    drinks.items.add(Item.objects.create(name='Cola light', price=175))
    drinks.items.add(Item.objects.create(name='Fanta', price=175))
    drinks.items.add(Item.objects.create(name='Sprite', price=175))
    drinks.items.add(Item.objects.create(name='Fernandez', price=175))
    
    drinks.items.add(Item.objects.create(name='Dr. Pepper', price=200))
    drinks.items.add(Item.objects.create(name='Blikje bier', price=200))
    drinks.items.add(Item.objects.create(name='Chocomel', price=200))
    drinks.items.add(Item.objects.create(name='Fristi', price=200))
    drinks.items.add(Item.objects.create(name='AA', price=200))

    drinks.items.add(Item.objects.create(name='Flesje Redbull', price=250))

    drinks.items.add(Item.objects.create(name='Milkshake aardbei (klein)', price=190))
    drinks.items.add(Item.objects.create(name='Milkshake aardbei (medium)', price=240))
    drinks.items.add(Item.objects.create(name='Milkshake aardbei (groot)', price=290))

    drinks.items.add(Item.objects.create(name='Milkshake vanille (klein)', price=190))
    drinks.items.add(Item.objects.create(name='Milkshake vanille (medium)', price=240))
    drinks.items.add(Item.objects.create(name='Milkshake vanille (groot)', price=290))

    drinks.items.add(Item.objects.create(name='Milkshake banaan (klein)', price=190))
    drinks.items.add(Item.objects.create(name='Milkshake banaan (medium)', price=240))
    drinks.items.add(Item.objects.create(name='Milkshake banaan (groot)', price=290))


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20150919_1646'),
    ]

    operations = [
        migrations.RunPython(add_drinks)
    ]
