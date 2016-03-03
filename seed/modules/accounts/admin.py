# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 0:46 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import flask
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.security.utils import encrypt_password

from seed import admin
from seed.core.admin import _l
from seed.modules.accounts.models import Role, User


class RoleAdmin(ModelView):
    page_size = 30
    can_create = True
    can_delete = False
    can_edit = True
    column_display_pk = False
    column_filters = ['name']
    column_exclude_list = ('created_at', 'updated_at',)
    column_default_sort = ('id', False)
    column_searchable_list = ('name', 'description',)
    column_labels = dict(
        id='ID',
        name='角色名称',
        description='角色描述',
        created_at='创建时间',
        updated_at='更新时间',
        users='包含以下用户')
    form_columns = ('name', 'description', 'created_at', 'updated_at', 'users')

    column_descriptions = dict(
        name='推荐使用英文名称，兼容性更强',
        description='简要的描述角色的作用',
        users='默认角色User中包含所有用户，请等候……')


class UserAdmin(ModelView):
    page_size = 30
    can_create = True
    can_delete = False
    can_edit = True
    column_display_pk = False
    column_filters = ['email']
    column_exclude_list = ('password', 'last_login_at', 'last_login_ip')
    column_default_sort = ('id', False)
    column_searchable_list = ('email',)
    column_labels = dict(
        id='ID',
        email='用户名',
        password='密码',
        active='启用',
        confirmed_at='确认时间',
        current_login_at='本次登录时间',
        current_login_ip='本次登录IP',
        last_login_at=u'上次登录时间',
        last_login_ip='上次登录IP',
        login_count='登录次数',
        roles='权限')

    column_descriptions = dict(
        email='用户登录标识',
        password='数据库将保存加密后的密码',
        active='是否启用帐户，默认为启用状态',
        roles='管理用户为Admin，普通用户为User，默认为User。'
    )

    form_choices = dict(
        roles=[dict(Admin='管理员'), dict(User='普通用户')],
    )

    create_template = 'admin/model/create_user.html'

    def create_model(self, form):
        self.model.register(
            email=form.data['email'],
            password=form.data['password'],
            confirmed=True,
            roles=['User']
        )
        return flask.redirect(flask.url_for('user.index_view'))

    def update_model(self, form, model):
        original_password = model.password
        model.update(**form.data)
        if form.data['password'] != original_password:
            model.password = encrypt_password(form.data['password'])
            model.save()
        return flask.redirect(flask.url_for('user.index_view'))


admin.register(Role, RoleAdmin, category=_l('Accounts'), name=_l('Roles'))
admin.register(User, UserAdmin, category=_l('Accounts'), name=_l('User'))
