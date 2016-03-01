# -*- coding: utf-8 -*-
# -*- date: 2016-03-01 0:38 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.babelex import gettext, ngettext, lazy_gettext


def _(*args, **kwargs):
    return gettext(*args, **kwargs)


def _n(*args, **kwargs):
    return ngettext(*args, **kwargs)


def _l(*args, **kwargs):
    return lazy_gettext(*args, **kwargs)
