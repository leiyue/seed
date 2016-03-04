#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.mistune import markdown

from seed.core.db import db
from seed.core.models.mixins import CRUD, Dated, ContentFormat


class Post(db.Model, CRUD, Dated, ContentFormat):
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(100), unique=True)
    summary = db.Column(db.String(255))
    body = db.Column(db.Text, nullable=False)

    def get_summary(self):
        if self.summary:
            return self.summary
        return self.get_text()

    def get_text(self):
        if hasattr(self, 'body'):
            text = self.body
        elif hasattr(self, 'description'):
            text = self.description
        else:
            text = self.summary or ''

        if self.content_format == 'markdown':
            return markdown(text)
        else:
            return text

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.title)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
