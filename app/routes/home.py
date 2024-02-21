from flask import current_app
from app.models import Post
from . import bp as home_bp

@home_bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)
