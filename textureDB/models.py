from django.db import models
from django.contrib.auth.models import User


class Texture(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(default='', max_length=255)
    rating = models.SmallIntegerField(default=0)
    added = models.DateTimeField()
    edited = models.DateTimeField()

    def __str__(self):
        return '{} by {}'.format(self.name, self.user)


class RealImage(models.Model):
    texture = models.ForeignKey(Texture)
    image = models.ImageField(upload_to='RealImage/%Y/%m/%d')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Real image for {}'.format(self.texture.name)


class RenderedImage(models.Model):
    texture = models.ForeignKey(Texture)
    image = models.ImageField(upload_to='RenderedImage/%Y/%m/%d')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Rendered image for {}'.format(self.texture.name)
