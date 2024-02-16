from flask import Flask
from app.routes.home import bp as home_bp
from app.routes.dashboard import bp as dashboard_bp
from app.db import init_db  # Import the init_db function
from app.utils import filters

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'

    # Register routes
    app.register_blueprint(home_bp)  # Adjusted this line to use home_bp directly
    app.register_blueprint(dashboard_bp)

    # Initialize the database
    init_db(app)

    return app

  