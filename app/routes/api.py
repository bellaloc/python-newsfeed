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
<<<<<<< HEAD
=======

@bp.route('/comments', methods=['POST'])
def comment():
    data = request.get_json()
    db = get_db()

    try:
        # create a new comment
        newComment = Comment(
            text=data['comment_text'],  # Use 'text' instead of 'comment_text'
            post_id=data['post_id'],
            user_id=session.get('user_id')
        )

        db.add(newComment)
        db.commit()
        return jsonify(id=newComment.id, message='Comment added successfully')
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Comment failed'), 500

@bp.route('/posts/upvote', methods=['PUT'])
def upvote():
    data = request.get_json()
    db = get_db()

    try:
        # create a new vote with incoming id and session id
        newVote = Vote(
            post_id=data['post_id'],
            user_id=session.get('user_id')
        )

        db.add(newVote)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Upvote failed'), 500

    return '', 204

@bp.route('/posts', methods=['POST'])
def create():
    data = request.get_json()
    db = get_db()

    try:
        # create a new post
        newPost = Post(
            title=data['title'],
            post_url=data['post_url'],
            user_id=session.get('user_id')
        )

        db.add(newPost)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post failed'), 500

    return jsonify(id=newPost.id)

@bp.route('/posts/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    db = get_db()

    try:
        # retrieve post and update title property
        post = db.query(Post).filter(Post.id == id).one()
        post.title = data['title']
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post not found'), 404

    return '', 204

@bp.route('/posts/<id>', methods=['DELETE'])
def delete(id):
    db = get_db()

    try:
        # delete post from db
        db.delete(db.query(Post).filter(Post.id == id).one())
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        return jsonify(message='Post not found'), 404

    return '', 204
>>>>>>> parent of d59795f (Merge pull request #16 from bellaloc/API)
