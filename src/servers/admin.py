from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Server, ServerAdmin)

