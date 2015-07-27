# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RealImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='RealImage/%Y/%m/%d')),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RenderedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='RenderedImage/%Y/%m/%d')),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Texture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, default='')),
                ('rating', models.SmallIntegerField(default=0)),
                ('added', models.DateTimeField()),
                ('edited', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='renderedimage',
            name='texture',
            field=models.ForeignKey(to='textureDB.Texture'),
        ),
        migrations.AddField(
            model_name='realimage',
            name='texture',
            field=models.ForeignKey(to='textureDB.Texture'),
        ),
    ]
