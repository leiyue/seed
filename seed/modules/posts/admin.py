#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-03-03 10:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model import InlineFormAdmin

from seed import admin
from seed.core.admin.utils import _l
from seed.core.admin.widgets import TextEditor, PrepopulatedText
from seed.modules.posts.models import Category, Post, Tag


class CategoryAdmin(ModelView):
    column_exclude_list = ('created_at', 'updated_at',)
    column_searchable_list = ('name',)
    column_labels = dict(
        id=_l('Id'),
        created_at=_l('Created At'),
        updated_at=_l('Updated At'),
        name=_l('Name'),
        description=_l('Description'),
        posts=_l('Posts')
    )
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True),
    )


class TagAdmin(ModelView):
    column_exclude_list = ('created_at', 'updated_at',)
    column_searchable_list = ('name',)
    column_labels = dict(
        id=_l('Id'),
        created_at=_l('Created At'),
        updated_at=_l('Updated At'),
        name=_l('Name'),
        posts=_l('Posts')
    )
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True),
    )


class TagInline(InlineFormAdmin):
    column_labels = dict(
        id=_l('Id'),
        created_at=_l('Created At'),
        updated_at=_l('Updated At'),
        name=_l('Name')
    )
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True),
    )


class PostAdmin(ModelView):
    column_auto_select_related = True
    form_choices = dict(
        content_format=[('html', 'html'), ('markdown', 'markdown'), ('text', 'text')],
    )
    form_args = dict(
        content={'widget': TextEditor()},
        slug={'widget': PrepopulatedText(master='title')}
    )
    form_widget_args = dict(
        created_at=dict(disabled=True),
        updated_at=dict(disabled=True),
    )
    inline_models = (TagInline(Tag),)


admin.register(Category, CategoryAdmin, category=_l('Content'), name=_l('Category'))
admin.register(Post, PostAdmin, category=_l('Content'), name=_l('Post'))
admin.register(Tag, TagAdmin, category=_l('Content'), name=_l('Tag'))
