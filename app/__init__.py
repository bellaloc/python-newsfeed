from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'

    # register routes
    from .routes.home import bp as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
