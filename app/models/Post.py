<<<<<<< HEAD
from datetime import datetime
from app.db import Base
from .Vote import Vote
from .Comment import Comment  # Import Comment model if not already imported
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
=======
# app/models/Post.py
from app.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
>>>>>>> main
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    comments = relationship("Comment", back_populates="post")  # Fix indentation
    votes = relationship('Vote', cascade='all,delete')
    
    @hybrid_property
    def vote_count(self):
        return len(self.votes)
=======
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
>>>>>>> main

    def __repr__(self):
        return f'<Post {self.title}>'
