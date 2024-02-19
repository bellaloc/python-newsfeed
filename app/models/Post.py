from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import select, func
from .Vote import Vote

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all,delete')
    votes = relationship('Vote', back_populates='post', cascade='all,delete')

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

