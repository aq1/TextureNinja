from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions

from textureDB.serializers import TextureSerializer, UserSerializer
from textureDB.models import Texture


class TextureViewSet(viewsets.ModelViewSet):
    queryset = Texture.objects.all()
    serializer_class = TextureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
