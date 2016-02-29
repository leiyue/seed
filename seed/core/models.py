# -*- coding: utf-8 -*-
# -*- date: 2016-02-29 23:47 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from seed.core.db import db


class Alembic(db.Model):
    __tablename__ = 'alembic_version'
    version_num = db.Column(db.String(32), primary_key=True, nullable=False)
