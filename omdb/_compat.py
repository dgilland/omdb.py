# flake8: noqa
# pylint: skip-file
"""Python 2/3 compatibility"""

from decimal import Decimal
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    text_type = unicode
    string_types = (str, unicode)
    number_types = (int, long, float, Decimal)

    def iterkeys(d): return d.iterkeys()

    def itervalues(d): return d.itervalues()

    def iteritems(d): return d.iteritems()
else:
    text_type = str
    string_types = (str,)
    number_types = (int, float, Decimal)

    def iterkeys(d): return iter(d.keys())

    def itervalues(d): return iter(d.values())

    def iteritems(d): return iter(d.items())
