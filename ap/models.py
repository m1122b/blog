
# ap/models.py


from ap import db
import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.datetime.utcnow)
    is_published = db.Column(db.Boolean, default=False)

