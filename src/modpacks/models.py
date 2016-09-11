from __future__ import unicode_literals

from django.db import models


class Mod(models.Model):
    """
    A mod that can be combined to make a modpack
    """

    mod_name = models.CharField(max_length=99, verbose_name='Mod Name')

    desc = models.TextField(
        verbose_name='Mod Description'
    )
    version = models.CharField(
        max_length=20,
        verbose_name='Mod Version'
    )
    author = models.CharField(max_length=99, verbose_name='Mod Author')


class Modpack(models.Model):
    """
    A combination of mods that can be run on a server/client
    """

    modpack_name = models.CharField(
        max_length=99,
        verbose_name='Mod Author'
    )
    desc = models.TextField(verbose_name='Mod Author')
    # image = # TODO: Image upload stuff?
    mods = models.ManyToManyField(
        Mod,
        blank=True,
        verbose_name='Mod Author'
    )
