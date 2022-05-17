
# ap/mydef.py


from flask import session, redirect, url_for, request
from ap.models import Post, db
import functools


def add_post(form):
    post = Post(
        title=form.title.data,
        body=form.body.data,
        is_published=form.is_published.data
        )
    db.session.add(post)
    db.session.commit()


def del_post(post_id):
    u=Post.query.get(post_id)
    db.session.delete(u)
    db.session.commit()


def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions


