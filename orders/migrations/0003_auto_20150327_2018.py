# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discounts',
            field=models.ManyToManyField(blank=True, to='orders.Discount'),
            preserve_default=True,
        ),
    ]
