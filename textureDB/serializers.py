from django.contrib.auth.models import User

from rest_framework import serializers

from textureDB.models import Texture


class TextureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Texture
        fields = ('url', 'author', 'title', 'rating', 'created', 'edited')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    textures = serializers.HyperlinkedRelatedField(
        queryset=Texture.objects.all(), view_name='texture-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'textures')
