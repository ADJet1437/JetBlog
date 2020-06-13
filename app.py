from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app 
app = Flask(__name__)

# Config
app.config.from_pyfile("config/base_setting.py")
# app db
db = SQLAlchemy(app)
