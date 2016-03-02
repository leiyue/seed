# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 22:57 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import Flask, Blueprint

from seed.core.config import SeedConfig


class SeedApp(Flask):
    config_class = SeedConfig

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return self.config_class(root_path, self.default_config)


class SeedModule(Blueprint):
    def __init__(self, name, *args, **kwargs):
        name = 'seed.modules.' + name
        super(SeedModule, self).__init__(name, *args, **kwargs)
