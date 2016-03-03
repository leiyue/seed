#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from seed.core.db import db
from seed.core.models.content import Content


class Post(Content):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.title)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
