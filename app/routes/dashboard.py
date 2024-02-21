from flask import Blueprint, render_template, session, abort
from app.models import Post
from app.db import get_db
from sqlalchemy.orm.exc import NoResultFound
from app.utils.auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
<<<<<<< HEAD
    db = get_db()
    posts = (
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template('dashboard.html', posts=posts, loggedIn=session.get('loggedIn'))
=======
    return render_template('dashboard.html')
>>>>>>> main

@bp.route('/edit/<int:id>')  
@login_required
def edit(id):
<<<<<<< HEAD
    if id is None:
        return "No post ID provided"
    
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()
    return render_template('edit-post.html', post=post, loggedIn=session.get('loggedIn'))

@bp.route('/post/<int:post_id>')
def single(post_id):
    try:
        db = get_db()
        post = db.query(Post).filter(Post.id == post_id).one()
        return render_template('post.html', post=post)
    except NoResultFound:
        abort(404)  # Handle case where post with given ID is not found
=======
    return render_template('edit-post.html')
>>>>>>> main
