''' Modpacks URL Configuration
'''

from django.conf.urls import url
from modpacks import views

app_name = "modpacks"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<slug>.+)/', views.modpack),
]
