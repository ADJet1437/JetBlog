from datetime import datetime
from flask import Flask, render_template, redirect, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flaskext.markdown import Markdown


# app 
app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/sqlite3-blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret'
# app db
db = SQLAlchemy(app)
Markdown(app)

# app admin
admin = Admin(app)


class BlogPost(db.Model):
    """Class for a sqlite3 table model
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    content = db.Column(db.Text)
    author = db.Column(db.String(30))
    post_date = db.Column(db.DateTime)


admin.add_view(ModelView(BlogPost, db.session))


@app.route('/')
def index():
  posts = BlogPost.query.order_by(BlogPost.post_date.desc()).all()

  return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
  post = BlogPost.query.filter_by(id=post_id).one()
  return render_template('post.html', post=post)


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/add')
def add():
  return render_template('add.html')


@app.route('/addpost', methods=['POST'])
def add_post():
  title = request.form.get('title')
  subtitle = request.form.get('subtitle')
  author = request.form.get('author')
  content = request.form.get('content')
  print(content)

  post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, post_date=datetime.now())
  # add data to database
  db.session.add(post)
  db.session.commit()

  return redirect(url_for('index'))


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
