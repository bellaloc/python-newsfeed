from datetime import datetime
from app.db import Base
from .Vote import Vote
from .Comment import Comment  # Import Comment model if not already imported
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
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

    @vote_count.expression
    def vote_count(cls):
        return (
            select([func.count(Vote.id)])
            .where(Vote.post_id == cls.id)
            .label('vote_count')
        )
