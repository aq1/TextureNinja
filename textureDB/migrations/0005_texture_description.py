# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0004_auto_20150728_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='texture',
            name='description',
            field=models.TextField(null=True, default=''),
        ),
    ]
