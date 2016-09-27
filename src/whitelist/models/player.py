from __future__ import unicode_literals
from django.db import models


class Player(models.Model):
    """A minecraft player, and their current whitelist status on the server
    """

    APPROVED = 'y'
    DENIED = 'n'
    PENDING = '?'
    WHITELIST_STATUS = (
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
        (PENDING, 'Pending'),)

    ign = models.CharField("In-Game Account Name",
                           max_length=50,
                           unique=True)
    status = models.CharField("Player Status",
                              max_length=1,
                              choices=WHITELIST_STATUS,
                              default=PENDING)
    email = models.EmailField("Email Address",
                              unique=True)

    def __str__(self):
        return self.ign
