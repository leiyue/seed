#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

import datetime

from flask.ext.mistune import markdown

from seed.core.db import db
from seed.core.models.base import CRUD, Timestamped, Dated, Formatted

posts_tags = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer(), db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id'))
)


class Category(db.Model, CRUD, Timestamped):
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Tag(db.Model, CRUD, Timestamped):
    name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Post(db.Model, CRUD, Timestamped, Dated, Formatted):
    title = db.Column(db.String(256), nullable=False)
    slug = db.Column(db.String(128), unique=True)
    summary = db.Column(db.String(256))
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.relationship('Category', backref='posts')
    author = db.relationship('User', backref='posts')
    tags = db.relationship(
        'Tag',
        enable_typechecks=False,
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def get_summary(self):
        if self.summary:
            return self.summary
        return self.get_text()

    def get_text(self):
        if hasattr(self, 'content'):
            text = self.content
        elif hasattr(self, 'description'):
            text = self.description
        else:
            text = self.summary or ''

        if self.content_format == 'markdown':
            return markdown(text)
        else:
            return text

    @property
    def is_available(self):
        now = datetime.datetime.now()
        return (
            self.published and self.available_at <= now and (
                self.available_until is None or self.available_until >= now
            )
        )

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.title)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
