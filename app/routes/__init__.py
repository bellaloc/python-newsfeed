from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db
from app.routes.home import home_bp
from app.routes.dashboard import dashboard_bp
from app.routes.api import api_bp

bp = Blueprint('home', __name__, url_prefix='/')
dashboard_bp = Blueprint('dashboard', __name__)
api_bp = Blueprint('api', __name__)

@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template(
        'homepage.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/login')
def login():
    # not logged in yet
    if session.get('loggedIn') is None:
        return render_template('login.html')

    return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        'single-post.html',
        post=post,
        loggedIn=session.get('loggedIn')
    )
