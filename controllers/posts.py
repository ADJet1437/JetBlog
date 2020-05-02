from flask import Blueprint, render_template

from common.db_models.blog_post import BlogPost

post_page = Blueprint("post_page", __name__)

@post_page.route('/post/<int:post_id>')
def post(post_id):
  post = BlogPost.query.filter_by(id=post_id).one()
  return render_template('post.html', post=post)