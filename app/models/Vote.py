from app.models import Base
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="votes")
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="votes")
    vote_type = Column(Enum('upvote', 'downvote'), nullable=False)

    def __repr__(self):
        return f'<Vote {self.vote_type}>'
