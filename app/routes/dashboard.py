from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db
from sqlalchemy.orm.exc import NoResultFound
from app.utils.auth import login_required

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
    db = get_db()
    posts = (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template('dashboard.html', posts=posts, loggedIn=session.get('loggedIn'))

@bp.route('/edit/<int:id>')
@login_required
def edit(id):
    if id is None:
        return "No post ID provided"
