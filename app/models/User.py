from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    _password = Column('password', String(100), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        assert len(password) > 4
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        return email
    
    def verify_password(self, password):
        return bcrypt.checkpw(
    password.encode('utf-8'),
    self.password.encode('utf-8')
  )
