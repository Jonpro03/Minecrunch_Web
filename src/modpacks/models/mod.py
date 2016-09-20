from __future__ import unicode_literals
from django.db import models


class Mod(models.Model):
    """
    A mod that can be combined to make a modpack
    """
    mod_name = models.CharField('Mod name',
                                max_length=200)
    version = models.CharField('Mod version',
                               max_length=10,
                               blank=True)
    author = models.CharField('Mod author',
                              max_length=200,
                              blank=True)
    url = models.URLField('Link to mod website',
                          blank=True)

    def __str__(self):
        return self.mod_name
