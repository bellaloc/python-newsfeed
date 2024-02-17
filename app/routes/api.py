from flask import Blueprint, request, jsonify
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()

    # create a new user
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    db = get_db()

    # save in database
    db.add(new_user)
    db.commit()

    # return user id
    return jsonify(id=new_user.id)
