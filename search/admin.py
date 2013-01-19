from django.contrib import admin
from search.models import Shortcut


class ShortcutAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_tag', 'short', 'description')


admin.site.register(Shortcut, ShortcutAdmin)
