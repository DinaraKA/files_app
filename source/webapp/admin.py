from django.contrib import admin
from webapp.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'file', 'name', 'author', 'date', 'access']
    list_filter = ['author', 'date', 'access']
    list_display_links = ['pk', 'name', 'author']


admin.site.register(File, FileAdmin)


