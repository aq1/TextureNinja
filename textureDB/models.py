from django.db import models
from django.contrib.auth.models import User


class Texture(models.Model):
    author = models.ForeignKey(User, related_name='textures')
    title = models.CharField(default='', max_length=255)
    description = models.TextField(null=True, default='')
    rating = models.SmallIntegerField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(null=True)

    def __str__(self):
        return '{} by {}'.format(self.name, self.author)


class RealImage(models.Model):
    texture = models.ForeignKey(Texture)
    image = models.ImageField(upload_to='textureDB/RealImage/%Y/%m/%d')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Real image for {}'.format(self.texture.name)


class RenderedImage(models.Model):
    texture = models.ForeignKey(Texture)
    image = models.ImageField(upload_to='textureDB/RenderedImage/%Y/%m/%d')
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Rendered image for {}'.format(self.texture.name)
