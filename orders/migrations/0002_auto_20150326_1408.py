# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='in_wie_betaald_wat',
        ),
        migrations.AddField(
            model_name='order',
            name='in_wie_betaalt_wat',
            field=models.BooleanField(default=True, verbose_name='Betaalt via Wiebetaaltwat'),
            preserve_default=True,
        ),
    ]
