from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from common.db_models.blog_post import BlogPost
from controllers.form import EditormdForm

add_post_endpoint = Blueprint("add_post_endpoint", __name__)

@add_post_endpoint.route('/addpost', methods=['POST'])
def add_post():
  title = request.form.get('title')
  subtitle = request.form.get('subtitle')
  author = request.form.get('author')
  content = request.form.get('blog-editor-markdown-doc')

  post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, post_date=datetime.now())
  # add data to database
  db.session.add(post)
  db.session.commit()

  return redirect(url_for('index_page.index'))