from flask import Blueprint, render_template

from common.db_models.blog_post import BlogPost

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
  posts = BlogPost.query.order_by(BlogPost.post_date.desc()).all()

  return render_template('index.html', posts=posts)