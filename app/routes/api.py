import sys
from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
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
            password=generate_password_hash(data['password'])
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
        if check_password_hash(user.password, data['password']):
            session.clear()
            session['user_id'] = user.id
            session['loggedIn'] = True
            return jsonify(id=user.id)
        else:
            return jsonify(message='Incorrect credentials'), 400
    except Exception as e:
        print(e)
        return jsonify(message='Incorrect credentials'), 400

@bp.route('/posts', methods=['GET'])
def get_posts():
    db = get_db()
    posts = db.query(Post).all()
    return jsonify(posts=[post.serialize() for post in posts])

@bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    db = get_db()
    post = db.query(Post).get(post_id)
    if post:
        return jsonify(post.serialize())
    else:
        return jsonify(message='Post not found'), 404

@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    db = get_db()

    try:
        new_post = Post(
            title=data['title'],
            content=data['content'],
            user_id=session.get('user_id')
        )

        db.add(new_post)
        db.commit()

        return jsonify(id=new_post.id)
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post creation failed'), 500

@bp.route('/posts/<int:post_id>/vote', methods=['POST'])
def vote_post(post_id):
    data = request.get_json()
    db = get_db()

    try:
        post = db.query(Post).get(post_id)
        if not post:
            return jsonify(message='Post not found'), 404

        vote = db.query(Vote).filter(
            Vote.post_id == post_id,
            Vote.user_id == session.get('user_id')
        ).first()

        if vote:
            return jsonify(message='You have already voted for this post'), 400

        new_vote = Vote(
            user_id=session.get('user_id'),
            post_id=post_id
        )

        db.add(new_vote)
        db.commit()

        return jsonify(id=new_vote.id)
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Voting failed'), 500

@bp.route('/comments', methods=['POST'])
def comment():
    data = request.get_json()
    db = get_db()

    try:
        new_comment = Comment(
            comment_text=data['comment_text'],
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
