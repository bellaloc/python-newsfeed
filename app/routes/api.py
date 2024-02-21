import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db
from app.utils.auth import login_required

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users/signup', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']  # Assuming 'password' is provided in the request data
        )

        db.add(new_user)
        db.commit()
        return jsonify(id=new_user.id), 201
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Signup failed'), 500

@bp.route('/users/logout', methods=['POST'])
def logout():
    session.clear()
    return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    try:
        user = db.query(User).filter(User.email == data['email']).one()
        if user.password == data['password']:
            session.clear()
            session['user_id'] = user.id
            return jsonify(id=user.id), 200
        else:
            return jsonify(message='Incorrect credentials'), 400
    except Exception as e:
        print(e)
        return jsonify(message='Login failed'), 500

@bp.route('/comments', methods=['POST'])
@login_required
def comment():
    data = request.get_json()
    db = get_db()
    try:
        # Create a new comment
        new_comment = Comment(
            text=data['comment_text'],  # Assuming 'text' is the correct attribute for comment text
            post_id=data['post_id'],
            user_id=session.get('user_id')
        )

        db.add(new_comment)
        db.commit()
        return jsonify(id=new_comment.id), 201
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Comment failed'), 500

# Define routes for posts, upvotes, create, update, delete...
