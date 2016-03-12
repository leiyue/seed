# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 9:57 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import flask
from flask.ext.security import current_user
from flask.ext.security.forms import (Form, NextFormMixin, EqualTo, email_required, email_validator, valid_user_email,
                                      unique_user_email,
                                      password_required, password_length, )
from flask.ext.security.utils import get_message, verify_and_update_password
from werkzeug.local import LocalProxy
from wtforms import StringField, PasswordField, BooleanField, SubmitField

from seed.core.admin.utils import _l

_datastore = LocalProxy(lambda: flask.current_app.extensions['security'].datastore)
_remember_default = LocalProxy(lambda: flask.current_app.config.get('SECURITY_DEFAULT_REMEMBER_ME', True))
_equal_to_new_password = EqualTo('new_password', message='RETYPE_PASSWORD_MISMATCH')
_confirm_password_equal = EqualTo('password', message='RETYPE_PASSWORD_MISMATCH')


class EmailField(object):
    email = StringField(_l('Email'), validators=[email_required, email_validator])


class ValidEmailField(object):
    email = StringField(_l('Email'), validators=[email_required, email_validator, valid_user_email])


class UniqueEmailField(object):
    email = StringField(_l('Email'), validators=[email_required, email_validator, unique_user_email])


class PasswordFieldMixin(object):
    password = PasswordField(_l('Password'), validators=[password_required])


class PasswordConfirmField(object):
    password_confirm = PasswordField(_l('Password Confirm'), validators=[_confirm_password_equal])


class ExtendedLoginForm(Form, NextFormMixin):
    user = None
    login_name = StringField(_l('Login Name'), validators=[email_required])
    password = PasswordField(_l('Password'), validators=[password_required])
    remember = BooleanField(_l('Remember'), default='checked' if _remember_default else None)
    submit = SubmitField(_l('Login'))

    def validate(self):
        if not super(ExtendedLoginForm, self).validate():
            return False

        if self.login_name.data.strip() == '':
            self.login_name.errors.append(get_message('EMAIL_NOT_PROVIDED')[0])
            return False

        if self.password.data.strip() == '':
            self.password.errors.append(get_message('PASSWORD_NOT_PROVIDED')[0])
            return False

        self.user = _datastore.get_user(self.login_name.data)

        if self.user is None:
            self.login_name.errors.append(get_message('USER_DOES_NOT_EXIST')[0])
            return False

        if not self.user.password:
            self.password.errors.append(get_message('PASSWORD_NOT_SET')[0])
            return False

        if not verify_and_update_password(self.password.data, self.user):
            self.password.errors.append(get_message('INVALID_PASSWORD')[0])
            return False

        if not self.user.is_active:
            self.login_name.errors.append(get_message('DISABLED_ACCOUNT')[0])
            return False

        return True


class ExtendedChangePasswordForm(Form, PasswordFieldMixin):
    new_password = PasswordField(_l('New Password'), validators=[password_required, password_length])

    new_password_confirm = PasswordField(_l('New Password Confirm'), validators=[_equal_to_new_password])

    submit = SubmitField(_l('Change Password'))

    def validate(self):
        if not super(ExtendedChangePasswordForm, self).validate():
            return False

        if not verify_and_update_password(self.password.data, current_user):
            self.password.errors.append(get_message('INVALID_PASSWORD')[0])
            return False
        if self.password.data.strip() == self.new_password.data.strip():
            self.password.errors.append(get_message('PASSWORD_IS_THE_SAME')[0])
            return False
        return True
