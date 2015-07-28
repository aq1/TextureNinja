from django.contrib.auth.models import User

from rest_framework import serializers

from textureDB.models import Texture, RealImage, RenderedImage


class TextureSerializer(serializers.HyperlinkedModelSerializer):
    # real_images = serializers.SlugRelatedField(many=True,
    #                                            read_only=True,
    #                                            slug_field='image')
    # rendered_images = serializers.SlugRelatedField(many=True,
    #                                                read_only=True,
    #                                                slug_field='image')

    real_images = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='RealImage-detail')

    class Meta:
        model = Texture
        fields = ('url', 'author', 'title', 'rating', 'created',
                  'edited', 'real_images')  # 'rendered_images')


class RealImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealImage
        fields = ('id', 'texture', 'image')


class RenderedImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RenderedImage
        fields = ('texture', 'image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    textures = serializers.HyperlinkedRelatedField(
        queryset=Texture.objects.all(), view_name='texture-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'textures')
