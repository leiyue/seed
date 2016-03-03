#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:06 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from seed.core.db import db
from seed.core.models.mixins import CRUD, Timestamp


class ContentTemplateType(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Content(db.Model, CRUD, Timestamp):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(255))
    content_template_type_id = db.Column(db.Integer, db.ForeignKey('content_template_type.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.title)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
