from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your SQLAlchemy models and Base class
from app.models.base import Base
from app.models.comment import Comment  # Import other models as needed

# Modify this line to import your database URL from your configuration
from python_newsfeed.config import DATABASE_URL

# Create a metadata object and associate it with your Base class
metadata = Base.metadata

# Set up logging configuration
fileConfig(context.config.config_file_name)

# Create the SQLAlchemy engine
engine = engine_from_config(
    context.config.get_section(context.config.config_ini_section),
    prefix='sqlalchemy.',
    url=DATABASE_URL
)

# Associate the engine with the metadata
context.configure(
    engine=engine,
    target_metadata=metadata
)
