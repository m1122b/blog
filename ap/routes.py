
# ap/routes.py


from flask import redirect, render_template, request, url_for
from ap import app
from ap.models import Post, db
from ap.forms import PostForm
from ap.mydef import add_post, del_post


@app.route("/", methods=["GET", "POST"])
def index():
    all_posts = Post.query.filter_by(is_published=True).order_by(Post.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts)


@app.route("/newpost/", methods=["GET", "POST"])
def create_post(): 
    form = PostForm()
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            add_post(form)
        else:
            errors = form.errors
        return redirect(url_for("index"))
    return render_template("newpostform.html", form=form, errors=errors)


@app.route("/editpost/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    form = PostForm(obj=post)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            add_post(form)
            del_post(post_id)
        else:
            errors = form.errors
        return redirect(url_for("index"))
    return render_template("editpostform.html", form=form, errors=errors)

