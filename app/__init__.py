import os
from flask import Flask
from dotenv import load_dotenv, dotenv_values
from app.routes import home_bp, dashboard_bp, api_bp
from app.db import init_db
from app.utils import filters

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Access specific environment variables
db_url = env_vars.get("DB_URL")

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    app.config.from_mapping(
        SECRET_KEY='super_secret_key',
        SQLALCHEMY_DATABASE_URI=db_url  # Assuming you're using SQLAlchemy for database connection
    )

    @app.route('/hello')
    def hello():
        return 'hello world'

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)

    # Initialize the database
    init_db(app)

    return app
