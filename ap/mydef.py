
# ap/mydef.py


from ap.models import Post, db


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


