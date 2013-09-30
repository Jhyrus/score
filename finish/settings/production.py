# -*- encoding; utf-8 -*-
from .base import *  # pyflakes.ignore

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Victor Aguilar @jvacx', 'jvacx.log@gmail.com'),
)

# Host and domains -------------------------------------------------------------

ALLOWED_HOSTS= [ 'localhost', '127.0.0.1' ]

# Sessions ---------------------------------------------------------------------

SESSION_EXPIRE_AT_BROWSER_CLOSE = True