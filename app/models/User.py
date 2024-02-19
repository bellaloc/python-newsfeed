from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    _password = Column('password', String(100), nullable=False)
    votes = relationship('Vote', back_populates='user')  # Assuming 'user' is the back reference name
    posts = relationship('Post', back_populates='user')  # Define relationship with Post model
    comments = relationship('Comment', back_populates='user')  # Add this line to establish the comments relationship

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        assert len(password) > 4
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))
