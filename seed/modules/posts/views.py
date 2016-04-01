# -*- coding: utf-8 -*-
# -*- date: 2016-03-12 10:48 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import render_template
from flask.views import MethodView

from seed.modules.posts.utils import get_posts, get_post


class ListView(MethodView):
    def get(self):
        posts = get_posts()
        return render_template('index.html', **locals())


class DetailView(MethodView):
    def get(self, post_id):
        post = get_post(post_id)
        return render_template('posts/post.html', **locals())
