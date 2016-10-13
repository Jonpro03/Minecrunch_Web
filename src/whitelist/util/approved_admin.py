from django.contrib import admin
from whitelist.models.player import Player


class ApprovedAdmin(admin.ModelAdmin):
    """ A ModelAdmin class that only shows approved players """
    def get_queryset(self, request):
        qs = super(ApprovedAdmin, self).get_queryset(request)
        return qs.filter(status=Player.APPROVED)
