# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 23:01 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir,
    'var',
    'db',
    'dev.db'))
