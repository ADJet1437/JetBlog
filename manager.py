# -*- coding: utf-8 -*-
from app import manager
from flask_script import Server, Command
from route import *
# from jobs.launcher import runJob

##web server
manager.add_command( "runserver", Server( host = "0.0.0.0", use_debugger=True, use_reloader= True ) )

# from jobs.movie import MovieJob
# manager.add_command( "runjob", MovieJob )
# manager.add_command( "runjob",runJob )


##create_table
@Command
def create_all():
    from app import db
    from common.db_models.blog_post import BlogPost
    db.create_all()

manager.add_command( "create_all", create_all )



def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()