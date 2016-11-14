from __future__ import unicode_literals
from django.db import models
from modpacks.models.modpack import Modpack


class Server(models.Model):
    """ Minecraft Server details for display on the server page """

    name = models.CharField(verbose_name='Server Name',
            max_length=200)
    modpack = models.ForeignKey(Modpack, verbose_name='Server Modpack')
    address = models.CharField(verbose_name='Server Address',
            max_length=200,
            blank=True)
    screenshot = models.ImageField(verbose_name='Screenshot',
            blank=True)
    dynmap = models.CharField(verbose_name='DynMap URL',
            max_length=200,
            blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("server", self.slug)

