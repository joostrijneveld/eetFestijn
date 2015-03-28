# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150327_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='in_wie_betaalt_wat',
            new_name='wiebetaaltwat',
        ),
    ]
