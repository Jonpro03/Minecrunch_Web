from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^modpacks', views.modpacks, name='modpacks'),
    url(r'^$', views.index, name='index'),
]