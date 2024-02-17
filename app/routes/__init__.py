from flask import Flask, Blueprint
from app.routes.home import bp as home_bp
from app.routes.dashboard import bp as dashboard_bp
from app.routes.api import bp as api_bp

# Create a new blueprint for API
api_blueprint = Blueprint('api', __name__)

# Register blueprints with the application
def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(api_blueprint)
