import sys
from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
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
            session['loggedIn'] = True
            return jsonify(id=user.id)
        else:
            return jsonify(message='Incorrect credentials'), 400
    except Exception as e:
        print(e)
        return jsonify(message='Incorrect credentials'), 400

@bp.route('/comments', methods=['POST'])
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
        return jsonify(id=new_comment.id)
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Comment failed'), 500

@bp.route('/posts/upvote', methods=['PUT'])
def upvote():
    data = request.get_json()
    db = get_db()

    try:
        new_vote = Vote(
            post_id=data['post_id'],
            user_id=session.get('user_id')
        )

        db.add(new_vote)
        db.commit()
        return '', 204
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Upvote failed'), 500

@bp.route('/posts', methods=['POST'])
def create():
    data = request.get_json()
    db = get_db()

    try:
        new_post = Post(
            title=data['title'],
            post_url=data['post_url'],
            user_id=session.get('user_id')
        )

        db.add(new_post)
        db.commit()
        return jsonify(id=new_post.id)
    except KeyError as e:
        return jsonify(message=f'Missing required field: {e.args[0]}'), 400
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post failed'), 500

@bp.route('/posts/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    db = get_db()

    try:
        post = db.query(Post).filter(Post.id == id).one()
        post.title = data['title']
        db.commit()
        return '', 204
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post not found'), 404

@bp.route('/posts/<id>', methods=['DELETE'])
def delete(id):
    db = get_db()

    try:
        db.delete(db.query(Post).filter(Post.id == id).one())
        db.commit()
        return '', 204
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post not found'), 404
