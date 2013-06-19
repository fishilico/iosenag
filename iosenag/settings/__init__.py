# -*- coding: utf-8 -*-
try:
    from .personal import *
except ImportError:
    from .dev import *