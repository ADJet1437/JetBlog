from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from common.libs.release_time import get_release_time

# app 
app = Flask(__name__)

# Config
app.config.from_pyfile("config/base_setting.py")
# app db
db = SQLAlchemy(app)


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
