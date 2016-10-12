from __future__ import unicode_literals
from django.db import models
from .player import Player


class ApprovedPlayer(Player):
    """A player that has been approved, and should be present on the whitelist.

    This is a proxy model, used for the admin section.
    """

    class Meta:
        proxy = True
        verbose_name = 'approved player'
