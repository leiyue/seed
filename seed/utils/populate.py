# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 11:19 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import json
import logging

from flask.ext.script import Command

from seed.core.db import db
from seed.modules.accounts.models import User, Role

logger = logging.getLogger()


class Populate(object):
    def __init__(self, db, *args, **kwargs):
        self.db = db
        self.args = args
        self.kwargs = kwargs
        self.roles = {}
        self.users = {}

    def __call__(self, *args, **kwargs):
        self.pipeline()

    def pipeline(self):
        self.load_existing_roles()
        self.load_existing_users()
        self.load_fixtures()
        self.create_users()

    def load_existing_roles(self):
        roles = Role.query.all()
        for role in roles:
            self.roles[role.name] = role

    def load_existing_users(self):
        users = User.query.all()
        for user in users:
            self.users[user.email] = user

    def load_fixtures(self):
        file_path = self.kwargs.get(
            'filepath',
            './etc/fixtures/initial_data.json'
        )
        with open(file_path) as f:
            self.json_data = json.load(f)

    def create_user(self, data):
        email = data.get('email')
        if email not in self.users:
            pwd = data.get('password')
            user = User.register(**data)
            self.users[email] = user
            logger.info('Created User: {0} {1}'.format(user.email, pwd))
            return user
        else:
            logger.info('User Existed: {0}'.format(email))

    def create_users(self, data=None):
        self.users_data = data or self.json_data.get('users')
        for data in self.users_data:
            self.create_user(data)


class PopulateCommand(Command):
    """Populate Database with Initial json data."""

    def run(self):
        Populate(db=db)()
