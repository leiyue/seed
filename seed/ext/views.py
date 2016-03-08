# -*- coding: utf-8 -*-
# -*- date: 2016-03-06 11:49 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import send_from_directory, current_app


def media(filename):
    return send_from_directory(
        current_app.config.get('MEDIA_ROOT'),
        filename
    )


def glyphicons_or_awesome(filename):
    if filename.startswith('glyphicons'):
        return send_from_directory(
            current_app.config.get('STATIC_ROOT'),
            filename='libs/bootstrap/fonts/' + filename
        )
    else:
        return send_from_directory(
            current_app.config.get('STATIC_ROOT'),
            filename='libs/font-awesome/fonts/' + filename
        )


def font_awesome(filename):
    return send_from_directory(
        current_app.config.get('STATIC_ROOT'),
        filename='libs/font-awesome/fonts/' + filename
    )


def summernote_font(filename):
    return send_from_directory(
        current_app.config.get('STATIC_ROOT'),
        filename='libs/summernote/dist/font/' + filename
    )


def configure(app):
    app.add_url_rule('/mediafiles/<path:filename>', view_func=media)
    app.add_url_rule('/static/fonts/<path:filename>', view_func=glyphicons_or_awesome)
    app.add_url_rule('/static/css/fonts/<path:filename>', view_func=font_awesome)
    app.add_url_rule('/static/css/admin/font/<path:filename>', view_func=summernote_font)
