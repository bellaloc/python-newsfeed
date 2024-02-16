from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# Load environment variables from .env file
load_dotenv()

# Connect to the database using the environment variable DB_URL
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

# Create a Session class bound to the engine
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()


def init_db(app):
    Base.metadata.create_all(engine)
    app.teardown_appcontext(close_db)


def get_db():
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()
    return g.db  # Add this line


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
