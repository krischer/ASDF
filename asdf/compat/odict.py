# Licensed under a 3-clause BSD style license - see LICENSE.rst


try:
    from collections import OrderedDict
except ImportError:
    from ._odict_py2 import *
