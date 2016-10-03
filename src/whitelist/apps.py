from __future__ import unicode_literals
from django.contrib import admin
from django.apps import AppConfig
from django.contrib.admin import sites


class WhitelistConfig(AppConfig):
    name = 'whitelist'

    def ready(self):
        """ Override the default 'ready' method to set up our custom admin page
        """

        # Define imports in here, as this function is only called when Django
        # is ready to define models
        from .util.approved_admin import ApprovedAdmin
        from .models.approved_player import ApprovedPlayer
        from .util.denied_admin import DeniedAdmin
        from .models.denied_player import DeniedPlayer
        from .util.pending_admin import PendingAdmin
        from .models.pending_player import PendingPlayer
        from .admin import WhitelistAdmin

        whitelist_admin = WhitelistAdmin(name='whitelistadmin')

        whitelist_admin.register(ApprovedPlayer, ApprovedAdmin)
        whitelist_admin.register(DeniedPlayer, DeniedAdmin)
        whitelist_admin.register(PendingPlayer, PendingAdmin)

        admin.site = whitelist_admin
        sites.site = whitelist_admin
