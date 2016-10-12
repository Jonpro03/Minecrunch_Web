from django.contrib import admin
from whitelist.models.player import Player


class DeniedAdmin(admin.ModelAdmin):
    """ A ModelAdmin class that only shows denied players """
    def get_queryset(self, request):
        qs = super(DeniedAdmin, self).get_queryset(request)
        return qs.filter(status=Player.DENIED)
