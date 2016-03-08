# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 22:43 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import render_template

from seed.core.admin import create_admin
from seed.core.app import SeedApp
from seed.ext import configure_extensions

admin = create_admin()


def create_base_app(config=None, **settings):
    app = SeedApp(__name__)
    app.config.load_config(config=config, **settings)
    return app


def create_app(config=None, admin_instance=None, **settings):
    app = create_base_app(config=config, **settings)

    configure_extensions(app, admin_instance or admin)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
