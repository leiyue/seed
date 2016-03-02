# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 22:53 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from seed.core.admin import configure_admin
from seed.core.db import db
from seed.ext import (loggers, babel, templates, security, blueprints, context_processors)


def configure_extensions(app, admin):
    loggers.configure(app)
    babel.configure(app)
    db.init_app(app)
    configure_admin(app, admin)
    templates.configure(app)
    security.configure(app, db)
    blueprints.load_from_folder(app)
    context_processors.configure(app)

    return app
