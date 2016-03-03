#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.admin.contrib.sqla import ModelView

from seed import admin
from seed.core.admin import _l
from seed.modules.posts.models import Post

admin.register(Post, ModelView, category=_l('Content'), name=_l('Post'))
