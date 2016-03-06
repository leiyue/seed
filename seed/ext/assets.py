# -*- coding: utf-8 -*-
# -*- date: 2016-03-06 19:39 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

from flask.ext.assets import Environment

env = Environment()


def configure(app):
    env.from_yaml(
        os.path.join(
            app.config.get('ROOT_DIR'),
            'etc',
            'assets',
            'vendor.yaml'
        )
    )

    env.from_yaml(
        os.path.join(
            app.config.get('ROOT_DIR'),
            'etc',
            'assets',
            'custom.yaml'
        )
    )
    env.init_app(app)
    env.app = app
