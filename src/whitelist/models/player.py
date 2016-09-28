from __future__ import unicode_literals
from django.db import models
from urllib2 import urlopen, HTTPError, URLError
import json


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
    BLANK_UUID = '00000000000000000000000000000000'

    ign = models.CharField("in-game account name",
                           max_length=50,
                           unique=True)
    status = models.CharField("player status",
                              max_length=1,
                              choices=WHITELIST_STATUS,
                              default=PENDING)
    email = models.EmailField("email address",
                              unique=True)
    uuid = models.UUIDField("Mojang UUID",
                            default=BLANK_UUID)

    def __str__(self):
        return self.ign

    def fetch_account_details(self):
        url = 'https://api.mojang.com/users/profiles/minecraft/{}'
        url = url.format(self.ign)

        try:
            response = urlopen(url)
            player_data = json.load(response)

            # Overwrite the player's provided name with the formatted version
            self.ign = player_data[u'name']
            self.uuid = player_data[u'id']

        except HTTPError, URLError:
            pass

    def save(self):
        if self.uuid.hex == self.BLANK_UUID:
            self.fetch_account_details()

        super(Player, self).save()

        return self
