from flask import Blueprint, render_template
from markdown import markdown
from common.db_models.blog_post import BlogPost

post_page = Blueprint("post_page", __name__)

@post_page.route('/post/<int:post_id>')
def post(post_id):
  post = BlogPost.query.filter_by(id=post_id).one()
  md_extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc']

  content = post.content
  content = markdown(content, extensions=md_extensions)
  return render_template('post.html', post=post, content=content)