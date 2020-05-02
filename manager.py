# -*- coding: utf-8 -*-
from route import app


def create_all():
    from app import db
    from common.db_models.blog_post import BlogPost
    from common.db_models.user import User
    db.create_all()


def main():
    app.run(debug=True)

if __name__ == "__main__":
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()