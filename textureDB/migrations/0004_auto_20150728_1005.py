# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0003_auto_20150727_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texture',
            old_name='user',
            new_name='author',
        ),
    ]
