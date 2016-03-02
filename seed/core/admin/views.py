# -*- coding: utf-8 -*-
# -*- date: 2016-03-01 0:13 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import current_app
from flask.ext.admin import AdminIndexView, expose, BaseView
from flask.ext.admin.contrib.fileadmin import FileAdmin as _FileAdmin
from flask.ext.admin.contrib.sqla import ModelView

from seed.core.admin import _l


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


class AlembicView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False
    column_display_pk = True
    column_labels = dict(
        version_num=_l('version_num')
    )


class FileAdmin(_FileAdmin):
    def __init__(self, *args, **kwargs):
        self.roles_accepted = kwargs.pop('roles_accepted', list())
        self.editable_extensions = kwargs.pop('editable_extensions', tuple())
        super(FileAdmin, self).__init__(*args, **kwargs)
