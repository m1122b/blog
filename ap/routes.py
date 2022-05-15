
# ap/routes.py


from flask import render_template
from ap import app
from ap.models import Post


@app.route("/")
def index():
    all_posts = Post.query.filter_by(is_published=True).order_by(Post.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts)


