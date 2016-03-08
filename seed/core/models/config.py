# -*- coding: utf-8 -*-
# -*- date: 2016-03-07 22:40 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import json

from seed.core.db import db
from seed.core.models.base import CRUD, Timestamped


def default_formatter(value):
    return value


class Value(db.Model, CRUD, Timestamped):
    DEFAULT_FORMATTER = default_formatter

    FORMATTERS = {
        'json': json.loads,
        'text': DEFAULT_FORMATTER,
        'int': int,
        'float': float
    }

    REVERSE_FORMATTERS = {
        'json': lambda val: val if isinstance(val, str) else json.dumps(val),
        'text': DEFAULT_FORMATTER,
        'int': DEFAULT_FORMATTER,
        'float': DEFAULT_FORMATTER
    }

    name = db.Column(db.String(128), unique=True, nullable=False)
    raw_value = db.Column(db.Text, nullable=False)
    formatter = db.Column(db.String(20), default='text')
    config_id = db.Column(db.Integer, db.ForeignKey('config.id'))

    @property
    def value(self):
        return self.FORMATTERS.get(self.formatter,
                                   self.DEFAULT_FORMATTER)(self.raw_value)

    @value.setter
    def value(self, value):
        self.raw_value = self.REVERSE_FORMATTERS.get(self.formatter,
                                                     self.STR_FORMATTER)(value)

    def __unicode__(self):
        return '{s.name} -> {s.value}'.format(s=self)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Config(db.Model, CRUD, Timestamped):
    group = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    values = db.relationship('Value', backref='config', lazy='dynamic')

    def get_value(self, name, default=None):
        try:
            return self.values.filter(Value.name == name).first().value
        except:
            return default

    def add_value(self, name, value, formatter='text'):
        Value.create(
            name=name,
            value=value,
            formatter=formatter,
            config_id=self.id
        )

    @classmethod
    def get(cls, group, name=None, default=None):
        try:
            instance = cls.find_one(group=group)
        except:
            return None

        if not name:
            ret = instance.values
        else:
            ret = instance.values.filter(Value.name == name).first().value

        return ret or default

    def __repr__(self):
        return '<{class_name}({name})>'.format(
            class_name=self.__class__.__name__, name=self.group)

    def __str__(self):
        return self.group

    def __unicode__(self):
        return self.group
