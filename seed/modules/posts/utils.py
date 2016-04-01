#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- date: 2016-04-02 01:10 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from seed.modules.posts.models import Post


def get_posts(*args, **kwargs):
    return Post.find(**kwargs)


def get_post(post_id):
    try:
        post = Post.find_one(id=post_id)
    except:
        post = Post.find_one(email=post_id)
    return post
