''' Modpacks URL Configuration
'''

from django.conf.urls import url
from modpacks import views

urlpatterns = [
    url(r'^/', views.index),
    url(r'^(?P<slug>.+)/', views.modpack),
    url(r'^mod/(?P<slug>.+)', views.mod),
]
