# -*- coding: utf-8 -*-
# -*- date: 2016-03-04 20:55 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import render_template
from wtforms.widgets import TextArea


class TextEditor(TextArea):
    def __init__(self, *args, **kwargs):
        super(TextEditor, self).__init__()
        self.css_cls = kwargs.get('css_cls', 'text_editor')

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{0} {1}'.format(self.css_cls, c)
        html = super(TextEditor, self).__call__(field, **kwargs)
        html += render_template(
            'admin/widgets/text_editor.html',
            selector='.' + self.css_cls
        )
        return html
