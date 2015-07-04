# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_receipt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='random_item',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
