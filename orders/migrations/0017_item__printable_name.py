# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_drinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='_printable_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
