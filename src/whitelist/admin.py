from django.contrib import admin
from .util.approved_admin import ApprovedAdmin
from .models.approved_player import ApprovedPlayer
from .util.denied_admin import DeniedAdmin
from .models.denied_player import DeniedPlayer
from .util.pending_admin import PendingAdmin
from .models.pending_player import PendingPlayer

admin.site.register(ApprovedPlayer, ApprovedAdmin)
admin.site.register(DeniedPlayer, DeniedAdmin)
admin.site.register(PendingPlayer, PendingAdmin)
