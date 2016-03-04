# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 0:32 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime
import logging

from seed.core.db import db

logger = logging.getLogger()


class CRUD(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def find_one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_or_create(cls, _commit=True, **kwargs):
        obj = cls.find_one(**kwargs)
        if not obj:
            obj = cls.create(_commit=_commit, **kwargs)
        return obj

    @classmethod
    def get_by_id(cls, obj_id):
        if any(
                (isinstance(obj_id, basestring) and obj_id.isdigit(),
                 isinstance(obj_id, (int, float))),
        ):
            return cls.query.get(int(obj_id))
        return None

    @classmethod
    def create(cls, _commit=True, **kwargs):
        instance = cls(**kwargs)
        obj = instance.save(_commit=_commit)
        logger.debug('Created {0}'.format(unicode(obj)))
        return obj

    def update(self, _commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return _commit and self.save() or self

    def save(self, _commit=True):
        db.session.add(self)
        if _commit:
            db.session.commit()
        return self

    def delete(self, _commit=True):
        db.session.delete(self)
        return _commit and db.session.commit()

    def __repr__(self):
        return '<{name}(id={id})>'.format(name=self.__class__.__name__, id=self.id)

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()


class Dated(object):
    available_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    available_until = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class ContentFormat(object):
    content_format = db.Column(db.String(20), default='html')
