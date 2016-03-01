# -*- coding: utf-8 -*-
# -*- date: 2016-03-01 0:13 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import current_app
from flask.ext.admin import AdminIndexView, expose, BaseView


class IndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/extended_index.html')


class InspectorView(BaseView):
    @expose('/')
    def index(self):
        context = {
            "app": current_app
        }
        return self.render('admin/inspector.html', **context)
