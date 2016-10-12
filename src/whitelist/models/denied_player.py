from __future__ import unicode_literals
from .player import Player


class DeniedPlayer(Player):
    """A player that has been denied a place on the whitelist, because they
    have made questionable decisions during their lives.

    This is a proxy model, used for the admin section.
    """

    class Meta:
        proxy = True
        verbose_name = 'denied player'
