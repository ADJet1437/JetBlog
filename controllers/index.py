from flask import Blueprint, render_template, request
from flask_paginate import Pagination, get_page_parameter, get_per_page_parameter

from common.db_models.blog_post import BlogPost

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    posts = BlogPost.query.order_by(BlogPost.post_date.desc()).all()

    posts, pagination = general_pagination(posts)

    return render_template('index.html', posts=posts, pagination=pagination)

def general_pagination(posts):
    # pagination
    PER_PAGE_DEFAULT = 5
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = request.args.get(get_per_page_parameter(), type=int,
                                default=PER_PAGE_DEFAULT)
    pagination = Pagination(page=page, total=len(posts), per_page=per_page,
                            search=False, record_name='posts', css_framework='bootstrap',
                            bs_version=4)
    begin = per_page * (page - 1)
    end = per_page * page
    if end > len(posts):
        end = len(posts)
    posts = posts[begin:end]
    return posts, pagination
