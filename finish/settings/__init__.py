# -*- encoding: utf-8 -*-
import sys
import os

DJANGO_ENVIRONMENT = os.environ.setdefault('DJANGO_ENVIRONMENT', 'develop')

if DJANGO_ENVIRONMENT == 'production':
    from .production import *
elif DJANGO_ENVIRONMENT == 'stage':
    from .stage import *
elif DJANGO_ENVIRONMENT == 'develop':
    from .develop import *
elif DJANGO_ENVIRONMENT == 'testing':
    from .testing import *
else:
    import sys
    sys.stderr.write('Unknow project environment "%s"\n' % DJANGO_ENVIRONMENT)
    sys.exit(1)


if DJANGO_ENVIRONMENT != 'testing':

    try:
        from local import *
    except ImportError:
        sys.stderr.write("Project has no local setting file settings/local.py\n")
        sys.exit(1)
