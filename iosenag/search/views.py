from django.shortcuts import redirect, render
from .models import Shortcut


def index(request):
    """Main view for search app"""
    query = (request.POST.get('q') or request.GET.get('q', '')).strip()
    short = (request.POST.get('short') or request.GET.get('short', '')).strip()
    shortcut = None

    # Split query if no shortcut is to selected
    if query and not short:
        q = query.split(' ', 1)
        short = q[0]
        query = q[1] if len(q) >= 2 else ''

    # Find shortcut
    if short:
        try:
            shortcut = Shortcut.objects.get(short=short)
            url = shortcut.get_url(query)
            return redirect(url)
        except Shortcut.DoesNotExist:
            query = (short + ' ' + query) if query else short
            short = ''

    return render(request, 'search.html', {
        'q': query,
        'short': short,
        'shortcuts': Shortcut.objects.order_by('short')})
