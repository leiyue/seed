# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 0:46 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import flask
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security.utils import encrypt_password

from seed import admin
from seed.core.admin.utils import _l
from seed.modules.accounts.models import Role, User


class RoleAdmin(ModelView):
    page_size = 30
    can_create = True
    can_delete = True
    can_edit = True

    column_filters = ['name']
    column_exclude_list = ('created_at', 'updated_at',)
    column_default_sort = ('id', False)
    column_searchable_list = ('name', 'description',)
    column_labels = dict(
        id=_l('Id'),
        created_at=_l('Created At'),
        updated_at=_l('Updated At'),
        name=_l('Name'),
        description=_l('Description'),
        users=_l('Users')
    )
    form_columns = ('name', 'description', 'created_at', 'updated_at', 'users')
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True)
    )


class UserAdmin(ModelView):
    page_size = 30
    can_create = True
    can_delete = True
    can_edit = True

    column_filters = ('email',)
    column_exclude_list = ('created_at', 'updated_at', 'password', 'last_login_at', 'last_login_ip',)
    column_default_sort = ('id', False)
    column_searchable_list = ('email',)
    column_labels = dict(
        id=_l('Id'),
        email=_l('Email'),
        password=_l('Password'),
        active=_l('Active'),
        created_at=_l('Created At'),
        updated_at=_l('Updated At'),
        confirmed_at=_l('Confirmed At'),
        current_login_at=_l('Current Login At'),
        current_login_ip=_l('Current Login Ip'),
        last_login_at=_l('Last Login At'),
        last_login_ip=_l('Last Login Ip'),
        login_count=_l('Login Count'),
        roles=_l('Roles'),
        posts=_l('Posts'),
    )
    column_descriptions = dict(
        email=_l('User login identify'),
        password=_l('Store the encrypted user password in database'),
        active=_l('Is the user enable'),
        roles=_l('admin for administrators group, user for users group, defaults to user')
    )
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True),
        confirmed_at=dict(disabled=True),
        current_login_at=dict(disabled=True),
        current_login_ip=dict(disabled=True),
        last_login_at=dict(disabled=True),
        last_login_ip=dict(disabled=True),
        login_count=dict(disabled=True),
    )

    def create_model(self, form):
        self.model.register(
            email=form.data['email'],
            password=form.data['password'],
            confirmed=True,
            roles=['user']
        )
        return flask.redirect(flask.url_for('user.index_view'))

    def update_model(self, form, model):
        original_password = model.password
        model.update(**form.data)
        if form.data['password'] != original_password:
            model.password = encrypt_password(form.data['password'])
            model.save()
        return flask.redirect(flask.url_for('user.index_view'))


admin.register(Role, RoleAdmin, category=_l('System'), name=_l('Roles'))
admin.register(User, UserAdmin, category=_l('System'), name=_l('User'))
