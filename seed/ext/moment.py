# -*- coding: utf-8 -*-
# -*- date: 2016-03-08 15:57 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.moment import Moment

moment = Moment()


def configure(app):
    moment.init_app(app)
