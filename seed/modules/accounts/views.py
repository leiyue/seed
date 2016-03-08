# -*- coding: utf-8 -*-
# -*- date: 2016-03-08 13:32 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import render_template
from flask.views import MethodView

from seed.modules.accounts.utils import get_users, get_user


class ListView(MethodView):
    def get(self, user_id):
        users = get_users()
        return render_template('accounts/list.html', **locals())


class ProfileView(MethodView):
    def get(self, user_id):
        user = get_user(user_id)
        return render_template('accounts/profile.html', **locals())
