# -*- coding: utf-8 -*-
from app import db
from route import app
from flask_script import Server, Command, Manager

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))

@Command
def create_all():
    from common.db_models.blog_post import BlogPost
    from common.db_models.user import User
    db.create_all()

@Command
def create_admin():
    from common.db_models.user import User
    from config.secret_setting import user_name, password, user_salt, password_salt

    model_user = User()
    model_user.user_name = user_name
    model_user.password = password
    model_user.user_salt = user_salt
    model_user.password_salt = password_salt

    db.session.add( model_user )
    db.session.commit()

manager.add_command("create_all", create_all)
manager.add_command("create_admin", create_admin)

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()