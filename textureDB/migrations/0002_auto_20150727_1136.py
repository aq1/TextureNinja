# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texture',
            old_name='added',
            new_name='created',
        ),
    ]
