from django.conf.urls import url
from textureDB import views

urlpatterns = [
    url(r'^$', views.TextureList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.TextureDetail.as_view()),
]
