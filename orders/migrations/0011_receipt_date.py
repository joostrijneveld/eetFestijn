# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=False,
        ),
    ]
