
# ap/routes.py


from flask import render_template, request
from ap import app
from ap.models import Post, db
from ap.forms import PostForm


@app.route("/")
def index():
    all_posts = Post.query.filter_by(is_published=True).order_by(Post.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts)


@app.route("/newpost/", methods=["GET", "POST"])
def create_post():
    form = PostForm()
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
                )
            db.session.add(post)
            db.session.commit()
        else:
            errors = form.errors
    return render_template("newpostform.html", form=form, errors=errors)



