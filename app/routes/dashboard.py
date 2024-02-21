<<<<<<< HEAD
from flask import Blueprint, render_template
=======
from flask import Blueprint, render_template, session, abort
from app.models import Post
from app.db import get_db
from sqlalchemy.orm.exc import NoResultFound
>>>>>>> parent of d59795f (Merge pull request #16 from bellaloc/API)

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

<<<<<<< HEAD
@bp.route('/edit/<id>')
=======
@bp.route('/edit/<int:id>')  
>>>>>>> parent of d59795f (Merge pull request #16 from bellaloc/API)
def edit(id):
    return render_template('edit-post.html')
