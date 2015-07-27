# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0002_auto_20150727_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realimage',
            name='image',
            field=models.ImageField(upload_to='textureDB/RealImage/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='renderedimage',
            name='image',
            field=models.ImageField(upload_to='textureDB/RenderedImage/%Y/%m/%d'),
        ),
    ]
