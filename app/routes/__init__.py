from flask import Flask
from app.routes.home import bp as home_bp
from app.routes.dashboard import bp as dashboard_bp
from .home import bp as home
from .dashboard import bp as dashboard
from app.routes import home, dashboard

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)
