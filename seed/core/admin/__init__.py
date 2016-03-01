# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 23:49 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from seed.core.admin.utils import _l
from seed.core.admin.views import IndexView, InspectorView
from seed.core.db import db
from seed.core.models import Alembic


def create_admin(app=None, index_view=None):
    return Admin(app=app, index_view=index_view or IndexView(), template_mode='bootstrap3')


def configure_admin(app, admin):
    admin.add_view(ModelView(Alembic, db.session, category=_l('System'), name=_l('Alembic')))
    admin.add_view(InspectorView(category=_l("Settings"), name=_l("Inspector")))
    if admin.app is None:
        admin.init_app(app)
    return admin
