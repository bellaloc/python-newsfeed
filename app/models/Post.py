from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
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

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    # Define the relationship with the User model
    author = relationship("User", back_populates="articles")
    
    # Define the relationship with the Comment model
    comments = relationship("Comment", back_populates="article")
