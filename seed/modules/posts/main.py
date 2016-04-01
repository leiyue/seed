#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:24 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from seed.core.app import SeedModule
from seed.modules.posts.views import ListView, DetailView

module = SeedModule('posts', __name__)

module.add_url_rule('/', view_func=ListView.as_view(str('list')))
module.add_url_rule('/posts/<int:post_id>', view_func=DetailView.as_view(str('detail')))
