from django.conf.urls import url
from textureDB import views

urlpatterns = [
    url(r'^$', views.texture_list),
    url(r'^(?P<pk>[0-9]+)/$', views.texture_detail),
]
