# -*- coding: utf-8 -*-
# -*- date: 2016-03-02 10:42 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.admin import helpers as admin_helpers


def configure(app):
    from seed import admin

    security = app.extensions.get('security')

    @security.context_processor
    def inject():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
        )
