from django.contrib.auth.models import User
# from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route

from textureDB.serializers import TextureSerializer, UserSerializer
from textureDB.models import Texture


class TextureViewSet(viewsets.ModelViewSet):
    queryset = Texture.objects.all()
    serializer_class = TextureSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    # def list(self, request):
    #     textures = Texture.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route(methods=['GET'])
    def detail(self, request, pk=None):
        pass


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
