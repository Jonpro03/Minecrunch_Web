from django.contrib import admin
from whitelist.models.player import Player


class PendingAdmin(admin.ModelAdmin):
    """ A ModelAdmin class that only shows players hanging in limbo, neither
    approved nor denied
    """
    def get_queryset(self, request):
        qs = super(PendingAdmin, self).get_queryset(request)
        return qs.filter(status=Player.PENDING)
