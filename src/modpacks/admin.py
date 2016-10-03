from django.contrib import admin
from modpacks.models.mod import Mod
from modpacks.models.modpack import Modpack


class ModpackAdmin(admin.ModelAdmin):
    '''
    Modpack admin: Make sure to prepopulate the slug field
    '''
    prepopulated_fields = {"slug": ("modpack_name",)}


admin.site.register(Mod)
admin.site.register(Modpack, ModpackAdmin)
