from flask import Flask
from app.routes.home import bp as home_bp
from app.routes.dashboard import bp as dashboard_bp

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)

    return app
