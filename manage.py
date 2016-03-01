# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 22:44 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell
from flask.ext.script.commands import ShowUrls

from seed import create_app
from seed.core.db import db

app = create_app()
migrate = Migrate(app, db)


def _make_context():
    return dict(app=app, db=db)


manager = Manager(app)
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('urls', ShowUrls)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    with app.app_context():
        manager.run()
