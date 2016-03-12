# -*- coding: utf-8 -*-
# -*- date: 2016-03-12 10:48 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import render_template
from flask.views import MethodView


class ListView(MethodView):
    def get(self):
        return render_template('index.html')
