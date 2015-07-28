# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('textureDB', '0005_texture_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texture',
            name='author',
            field=models.ForeignKey(related_name='textures', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='texture',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='texture',
            name='edited',
            field=models.DateTimeField(null=True),
        ),
    ]
