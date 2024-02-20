from app import create_app
from app.routes.api import bp as api_bp  # Import the api_bp blueprint

app = create_app()

# Register the api_bp blueprint with the app
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
