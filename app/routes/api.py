import sys
from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        # attempt creating a new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.add(new_user)
        db.commit()

        session.clear()
        session['user_id'] = new_user.id
        session['loggedIn'] = True

        return jsonify(id=new_user.id)
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Signup failed'), 500

@bp.route('/users/logout', methods=['POST'])
def logout():
    # remove session variables
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    try:
        user = db.query(User).filter(User.email == data['email']).one()
        # Check if password matches
        if user.password == data['password']:
            session.clear()
            session['user_id'] = user.id
            session['loggedIn'] = True
            return jsonify(id=user.id)
        else:
            return jsonify(message='Incorrect credentials'), 400
    except Exception as e:
        print(e)
        return jsonify(message='Incorrect credentials'), 400
