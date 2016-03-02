# -*- coding: utf-8 -*-
# -*- date: 2016-03-01 10:45 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import sys

from flask import Blueprint
from werkzeug.routing import Rule
from wtforms import HiddenField

if sys.version_info.major == 3:
    unicode = lambda x: '{}'.format(x)
    basestring = str  # noqa

basetypes = (
    int, str, float, dict, list, tuple,
    Blueprint, Rule,
    basestring, unicode,
)


def is_instance(v, cls):
    cls_map = {
        tp.__name__: tp for tp in basetypes
        }
    return isinstance(v, cls_map.get(cls, str))


def is_hidden_field_filter(field):
    return isinstance(field, HiddenField)


def configure(app):
    app.jinja_env.filters['isinstance'] = is_instance
    app.jinja_env.globals['is_hidden_field'] = is_hidden_field_filter
