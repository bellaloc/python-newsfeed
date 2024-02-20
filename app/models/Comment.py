from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

    def __init__(self, text, user_id, post_id):
        self.text = text
        self.user_id = user_id
        self.post_id = post_id
