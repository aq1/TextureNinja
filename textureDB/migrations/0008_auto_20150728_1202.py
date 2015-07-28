# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0007_auto_20150728_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realimage',
            name='texture',
            field=models.ForeignKey(to='textureDB.Texture', related_name='real_images'),
        ),
        migrations.AlterField(
            model_name='renderedimage',
            name='texture',
            field=models.ForeignKey(to='textureDB.Texture', related_name='rendered_images'),
        ),
    ]
