from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    _password = Column('password', String(100), nullable=False)
    
    # Define the relationship with the Article model
    articles = relationship("Article", back_populates="author")
    
    # Define the relationship with the Comment model
    comments = relationship("Comment", back_populates="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        assert len(password) > 4
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))

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

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))
    
    # Define the relationship with the User model
    user = relationship("User", back_populates="comments")
    
    # Define the relationship with the Article model
    article = relationship("Article", back_populates="comments")

# Create an engine
engine = create_engine('sqlite:///blog.db')

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
