from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.http import urlquote_plus
import re
import os

ICON_BASE_PATH = os.path.join(settings.STATIC_ROOT, 'icons')
ICON_BASE_URL = settings.STATIC_URL + 'icons/'
DEFAULT_ICON = 'void.png'

# Search-in functionality
SEARCH_IN_PREFIX = 'search-in:'
SEARCH_IN_TEMPLATE = 'https://www.google.com/search?q=site:{site}+{q}'


class Shortcut(models.Model):
    """Search shortcut"""
    short = models.CharField(max_length=10, primary_key=True)
    short.help_text = "Shortcut (short text)"

    name = models.CharField(max_length=30, unique=True)
    short.help_text = "Name of the shortcut"

    icon = models.CharField(max_length=30, blank=True)
    icon.help_text = "Path to an icon file"

    template = models.CharField(max_length=100)
    template.help_text = ("http://example.com/?query={q} or "
                          "%shttp://example.com/" % SEARCH_IN_PREFIX)

    def __unicode__(self):
        return self.name

    def safe_name(self):
        """Return a safe version of the name"""
        return re.sub(r'[^a-zA-Z0-9 ._-]', '', self.name)

    def icon_url(self):
        """URL to the icon"""
        icon = self.icon if self.icon else DEFAULT_ICON
        icon = re.sub(r'[^a-zA-Z0-9._-]', '', icon)
        return ICON_BASE_URL + icon

    def icon_tag(self):
        """HTML tag to view the icon"""
        return mark_safe(u'<img border="0" width="16px" height="16px"' +
                u' src="%s" alt="%s" />' %
                (self.icon_url(), self.name))
    icon_tag.allow_tags = True
    icon_tag.admin_order_field = 'icon'

    def get_url(self, query=None):
        """Get an URL from the query"""
        url = self.template
        if url.startswith(SEARCH_IN_PREFIX):
            url = url[len(SEARCH_IN_PREFIX):]
            url = SEARCH_IN_TEMPLATE.replace('{site}', urlquote_plus(url))
        return url.replace('{q}', urlquote_plus(query) if query else '')
