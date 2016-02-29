# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 22:58 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

import yaml
from flask import Config


class SeedConfig(Config):
    def from_yaml(self, filename, silent=False):
        filename = os.path.join(self.root_path, filename)
        try:
            with open(filename) as config_file:
                c = yaml.load(config_file)
        except Exception as e:
            if silent:
                return False
            e.message = 'Unable to load ymal configuration: {0}'.format(
                filename
            )
            raise
        env = os.environ.get('FLASK_ENV', 'DEVELOPMENT').upper()
        self['ENVIRONMENT'] = env.lower()

        c = c.get(env, c)
        self.update(c)

    def load_config(self, config=None, **settings):
        self.from_yaml('../etc/conf/settings.yaml')
        self.from_object(config or 'seed.settings')
        self.update(settings)
