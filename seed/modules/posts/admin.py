#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.admin.contrib.sqla import ModelView

from seed import admin
from seed.core.admin import _l
from seed.core.admin.widgets import TextEditor
from seed.modules.posts.models import Category, Post


class PostAdmin(ModelView):
    form_choices = dict(
        content_format=[('html', 'html'), ('markdown', 'markdown'), ('text', 'text')],
    )
    form_args = dict(
        content={'widget': TextEditor()}
    )

admin.register(Category, ModelView, category=_l('Content'), name=_l('Category'))
admin.register(Post, PostAdmin, category=_l('Content'), name=_l('Post'))
