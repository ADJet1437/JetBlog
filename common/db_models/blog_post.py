from app import db

class BlogPost(db.Model):
    """Class for a sqlite3 table model
    """
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    content = db.Column(db.Text)
    author = db.Column(db.String(30))
    post_date = db.Column(db.DateTime)