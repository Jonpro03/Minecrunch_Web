from __future__ import unicode_literals
from django.db import models
from .mod import Mod


class Modpack(models.Model):
    """
    A combination of mods that can be run on a server/client
    """
    modpack_name = models.CharField(verbose_name='Modpack Name',
                                    max_length=200)
    desc = models.TextField(verbose_name='Description of modpack',
                            blank=True)
    image = models.ImageField(verbose_name='Screenshot',
                              blank=True)
    mods = models.ManyToManyField(Mod,
                                  verbose_name='Included mods',
                                  blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.modpack_name
