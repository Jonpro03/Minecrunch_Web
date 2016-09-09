from __future__ import unicode_literals

from django.db import models


class Mod(models.Model):
    """
    A mod that can be combined to make a modpack
    """

    desc = models.CharField(max_length=99)
    version = models.CharField(max_length=20)
    author = models.CharField(max_length=99)


class Modpack(models.Model):
    """
    A combination of mods that can be run on a server/client
    """
    
    desc = models.CharField(max_length=99)
    #image = # TODO: Image upload stuff
    mods = models.ManyToManyField(Mod, blank=True)    