from __future__ import unicode_literals

from django.db import models


class Player(models.Model):
    """A minecraft player, and their current whitelist status on the server
    """

    APPROVED = 'y'
    DENIED = 'n'
    WHITELIST_STATUS = (
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
        )

    ign = models.CharField(verbose_name="In-Game Account Name",
                           max_length=50)
    status = models.CharField(verbose_name="Player Status",
                              max_length=1,
                              blank=True)
    email = models.EmailField(verbose_name="Email Address")
