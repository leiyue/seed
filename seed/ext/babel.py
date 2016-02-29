# -*- coding: utf-8 -*-
# -*- date: 2016-03-01 0:23 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.babelex import Babel

babel = Babel()


def configure(app):
    babel.init_app(app)
