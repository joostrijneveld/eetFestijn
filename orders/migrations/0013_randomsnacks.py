# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def random_snacks(apps, schema_editor):
    Category = apps.get_model("orders", "Category")
    snacks = Category.objects.get(name='Snacks')
    snacks.random_item = "Willekeurige snack"
    snacks.save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_category_random_item'),
    ]

    operations = [
        migrations.RunPython(random_snacks)
    ]
