
# ap/routes.py


from flask import redirect, render_template, request, url_for, session, flash
from ap import app
from ap.models import Post, db
from ap.forms import PostForm, LoginForm
from ap.mydef import add_post, del_post, login_required


@app.route("/", methods=["GET", "POST"])
def index():
    all_posts = Post.query.filter_by(is_published=True).order_by(Post.pub_date.desc())

    return render_template("homepage.html", all_posts=all_posts)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("loginform.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'success')
    return redirect(url_for('index'))


@app.route("/newpost/", methods=["GET", "POST"])
@login_required
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
@login_required
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


