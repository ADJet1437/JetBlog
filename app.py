from datetime import datetime
from flask import Flask, render_template, redirect, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from common.libs.release_time import get_release_time

# app 
app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/sqlite3-blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret'
# app db
db = SQLAlchemy(app)

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

class User(db.Model):
    """Class for a sqlite3 table model
    """
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(50))


admin.add_view(ModelView(BlogPost, db.session))


class UrlManager(object):

    @staticmethod
    def buildUrl(path):
        # TODO: move to conf file
        domain_name = "http://0.0.0.0:5001"
        return "%s%s" % (domain_name, path)

    @staticmethod
    def buildStaticUrl(path):
        """

        :param path:
        :return:
        """
        release = get_release_time() 
        path = "/static" + path + '?v=' + release
        return UrlManager.buildUrl( path )

# Global template funtions
app.add_template_global(UrlManager.buildUrl, "buildUrl")
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")

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

  post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, post_date=datetime.now())
  # add data to database
  db.session.add(post)
  db.session.commit()

  return redirect(url_for('index'))


@app.route("/login")
def login():
  return render_template("login.html")


if __name__ == "__main__":
   db.create_all()
   app.run(host='0.0.0.0', port='5001', debug=True)
