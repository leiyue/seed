# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 23:49 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from seed.core.admin.utils import _l
from seed.core.admin.views import IndexView, InspectorView, AlembicView, FileAdmin, ConfigAdmin
from seed.core.db import db
from seed.core.models.alembic import Alembic
from seed.core.models.config import Config


class SeedAdmin(Admin):
    registered = []

    def register(self, model, view=None, *args, **kwargs):
        _view = view or ModelView
        admin_view_exclude = []
        identifier = '.'.join((model.__module__, model.__name__))
        if (identifier not in admin_view_exclude) and (
                    identifier not in self.registered):
            self.add_view(_view(model, db.session, *args, **kwargs))
            self.registered.append(identifier)


def create_admin(app=None, index_view=None):
    return SeedAdmin(
        app=app,
        base_template='admin/extended_base.html',
        index_view=index_view or IndexView(),
        template_mode='bootstrap3'
    )


def configure_admin(app, admin):
    admin.add_view(AlembicView(Alembic, db.session, category=_l('System'), name=_l('Alembic')))
    admin.add_view(InspectorView(category=_l("Settings"), name=_l("Inspector")))
    admin.add_view(ConfigAdmin(Config, db.session, category=_l("Settings"), name=_l("Config")))

    for entry in app.config.get('FILE_ADMIN', []):
        try:
            admin.add_view(
                FileAdmin(
                    entry['path'],
                    entry['url'],
                    name=entry['name'],
                    category=entry['category'],
                    endpoint=entry['endpoint'],
                    roles_accepted=entry.get('roles_accepted'),
                    editable_extensions=entry.get('editable_extensions')
                )
            )
        except Exception as e:
            app.logger.info(e)

    if admin.app is None:
        admin.init_app(app)
    return admin
