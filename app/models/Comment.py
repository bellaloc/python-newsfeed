<<<<<<< HEAD
from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
=======
# app/models/Comment.py
from app.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
>>>>>>> main
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = 'comments'
<<<<<<< HEAD
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(1000), nullable=False)
=======

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
>>>>>>> main
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="comments")
    post_id = Column(Integer, ForeignKey('posts.id'))
<<<<<<< HEAD
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

    def __init__(self, text, user_id, post_id):
        self.text = text
        self.user_id = user_id
        self.post_id = post_id
=======
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f'<Comment {self.content}>'
>>>>>>> main
