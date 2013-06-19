# Save data in a Python format
if __name__ == '__main__':
    import os
    import sys
    path = os.path.dirname(os.path.dirname(__file__))
    if path not in sys.path:
        sys.path.append(path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iosenag.settings")

from search.models import Shortcut


def save_all():
    print('from search.models import Shortcut')
    for obj in Shortcut.objects.order_by('short'):
        concrete_model = obj._meta.concrete_model
        fields = []
        for field in concrete_model._meta.local_fields:
            val = str(field._get_val_from_obj(obj))
            fields.append('%s=%s' % (field.name, repr(val)))
        print('Shortcut(%s).save()' % (', '.join(fields)))


if __name__ == '__main__':
    save_all()
