from flask import Flask
from app.routes import home, dashboard, api  # Importing blueprints from routes package
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

    # Register blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(api.bp)

    # Initialize the database
    init_db(app)

    return app
