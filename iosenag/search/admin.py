from django.contrib import admin
from .models import Shortcut


class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_tag', 'short', 'template')
    ordering = ['short']


admin.site.register(Shortcut, ShortcutAdmin)
