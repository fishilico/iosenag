from django.shortcuts import render


def mirror(request):
    # Find HTTP headers
    http_headers = {}
    for name, value in request.META.items():
        if name.startswith('HTTP_'):
            name = '-'.join([s.capitalize() for s in name[5:].split('_')])
            http_headers[name] = value

    context = {
        'request': request,
        'meta': request.META,
        'http_headers': sorted(http_headers.items())}
    return render(request, 'mirror.html', context)
