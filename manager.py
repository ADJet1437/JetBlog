# -*- coding: utf-8 -*-
from route import app
from flask_script import Server, Command, Manager

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", use_debugger=True, use_reloader=True))

@Command
def create_all():
    from app import db
    from common.db_models.blog_post import BlogPost
    from common.db_models.user import User
    db.create_all()

manager.add_command("create_all", create_all)

def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()