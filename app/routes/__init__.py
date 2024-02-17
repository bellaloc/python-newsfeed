from flask import Blueprint

# Import blueprints from respective modules
from .home import bp as home_bp
from .dashboard import bp as dashboard_bp
from .api import bp as api_bp

# Create a new blueprint for API
api_blueprint = Blueprint('api', __name__)

# Register blueprints with the application
def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(api_blueprint)
