"""Whitelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from .views import index
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = "whitelist"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^submitted$',
        TemplateView.as_view(template_name='whitelist/submitted.html'),
        name='submitted'),
]
