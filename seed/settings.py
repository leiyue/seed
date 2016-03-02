# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 23:01 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

from seed.core.admin.utils import _, _l

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediafiles')

SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir,
    'var',
    'db',
    'dev.db'))

DEFAULT_EDITABLE_EXTENSIONS = (
    'html', 'css', 'js', 'py', 'txt', 'md', 'cfg', 'coffee', 'html', 'json',
    'xml', 'yaml', 'yml',
)

FILE_ADMIN = [
    {
        'name': _l('Static files'),
        'category': _l('Files'),
        'path': STATIC_ROOT,
        'url': '/static/',  # create nginx rule
        'endpoint': 'static_files',
        'roles_accepted': ('admin', 'editor'),
        'editable_extensions': DEFAULT_EDITABLE_EXTENSIONS
    },
    {
        'name': _l('Media files'),
        'category': _l('Files'),
        'path': MEDIA_ROOT,
        'url': '/mediafiles/',  # Create nginx rule
        'endpoint': 'media_files',
        'roles_accepted': ('admin', 'editor'),
        'editable_extensions': DEFAULT_EDITABLE_EXTENSIONS
    }
]
