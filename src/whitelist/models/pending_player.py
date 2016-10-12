from __future__ import unicode_literals
from django.db import models
from .player import Player


class PendingPlayer(Player):
    """A player that awaits judgement.

    This is a proxy model, used for the admin section.
    """

    class Meta:
        proxy = True
        verbose_name = 'pending player'
