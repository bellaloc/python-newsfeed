from .db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="comments")
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f'<Comment {self.content}>'
