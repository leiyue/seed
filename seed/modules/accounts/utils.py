# -*- coding: utf-8 -*-
# -*- date: 2016-03-08 13:56 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from seed.modules.accounts.models import User


def get_users(*args, **kwargs):
    return User.find(**kwargs)


def get_user(user_id):
    try:
        user = User.find_one(id=user_id)
    except:
        user = User.find_one(email=user_id)
    return user
