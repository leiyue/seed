# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 0:32 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime

import flask
from flask.ext.security import RoleMixin, UserMixin
from flask.ext.security.utils import encrypt_password
from werkzeug.local import LocalProxy

from seed.core.db import db
from seed.core.models.mixins import CRUD, Timestamp

_security = LocalProxy(lambda: flask.current_app.extensions.get('security'))

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin, CRUD, Timestamp):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<{class_name}({name})>'.format(
            class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class User(db.Model, UserMixin, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    current_login_ip = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer(), default=0)
    roles = db.relationship('Role',
                            enable_typechecks=False,
                            secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.email)

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def confirm(self):
        self.confirmed_at = datetime.datetime.now()
        self.active = True
        self.save()

    def add_role(self, role_name):
        new_role = _security.datastore.find_or_create_role(role_name)
        _security.datastore.add_role_to_user(self, new_role)
        db.session.commit()

    @classmethod
    def register(cls, email, password, confirmed=False, roles=None):

        new_user = _security.datastore.create_user(
            email=email,
            password=encrypt_password(password)
        )
        db.session.commit()
        if confirmed:
            new_user.confirm()
        if roles:
            for role_name in roles:
                new_user.add_role(role_name)
        flask.current_app.logger.debug('Created user {0}'.format(email))
        return new_user

    @classmethod
    def add_system_users(cls):

        # make roles
        _security.datastore.find_or_create_role('admin')
        _security.datastore.find_or_create_role('user')
        db.session.commit()

        cls.register(email='admin', password='123', confirmed=True, roles=['admin'])
        cls.register(email='guest', password='guest', confirmed=True, roles=['user'])
        db.session.commit()

    @classmethod
    def rm_system_users(cls):
        _security.datastore.delete_user(email='admin')
        _security.datastore.delete_user(email='guest')
        db.session.commit()
