from datetime import datetime
from functools import wraps

from flask import Flask, render_template, redirect, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user

from common.libs.release_time import get_release_time

# app 
app = Flask(__name__)

import os

current_path = os.getcwd()
db_path = current_path + '/db'

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}/sqlite3-blog.db".format(db_path)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret'
# app db
db = SQLAlchemy(app)


# class BlogPost(db.Model):
#     """Class for a sqlite3 table model
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     subtitle = db.Column(db.String(50))
#     content = db.Column(db.Text)
#     author = db.Column(db.String(30))
#     post_date = db.Column(db.DateTime)


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


if __name__ == "__main__":
  #  db.create_all()
   app.run(host='0.0.0.0', port='5000', debug=True)
