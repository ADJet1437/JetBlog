from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from common.libs.release_time import get_release_time

# app 
app = Flask(__name__)

# Config
app.config.from_pyfile("config/base_setting.py")
# app db
db = SQLAlchemy(app)
