from django.contrib import admin


class ModpackAdmin(admin.ModelAdmin):
    '''
    Modpack admin: Make sure to prepopulate the slug field
    '''
    prepopulated_fields = {"slug": ("modpack_name",)}
