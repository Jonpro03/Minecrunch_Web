from __future__ import unicode_literals
from django.db import models


class Mod(models.Model):
    """
    A mod that can be combined to make a modpack
    """
    mod_name = models.CharField(verbose_name='Mod name',
                                max_length=200)
    version = models.CharField(verbose_name='Mod version',
                               max_length=10)
    author = models.CharField(verbose_name='Mod author',
                              max_length=200)
    url = models.URLField(verbose_name='Link to mod website',
                          blank=True)


class Modpack(models.Model):
    """
    A combination of mods that can be run on a server/client
    """
    modpack_name = models.CharField(verbose_name='Modpack Name',
                                    max_length=200)
    desc = models.TextField(verbose_name='Description of modpack',
                            blank=True)
    # image = # TODO: Image upload stuff?
    mods = models.ManyToManyField(Mod,
                                  verbose_name='Included mods',
                                  blank=True)
    slug = models.SlugField()
