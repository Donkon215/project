from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import Blueprints
    from app.home import home_bp
    from app.map import map_bp

    # Register Blueprints
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(map_bp, url_prefix='/map_view')

    return app
