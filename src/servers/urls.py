''' Servers URL Configuration
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="servers"),
    url(r'^(?P<slug>.+)/', views.server, name="server"),
]
