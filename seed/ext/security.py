# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 9:55 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.security import Security, SQLAlchemyUserDatastore

from seed.modules.accounts.forms import ExtendedLoginForm, ExtendedChangePasswordForm
from seed.modules.accounts.models import User, Role

security = Security()


def configure(app, db):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(
        app, datastore=user_datastore,
        login_form=ExtendedLoginForm,
        change_password_form=ExtendedChangePasswordForm
    )
