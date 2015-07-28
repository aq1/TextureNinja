# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0006_auto_20150728_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texture',
            name='rating',
            field=models.SmallIntegerField(default=0, null=True),
        ),
    ]
