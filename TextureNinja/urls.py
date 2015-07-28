from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from textureDB import views

router = DefaultRouter()
router.register(r'textures', views.TextureViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
