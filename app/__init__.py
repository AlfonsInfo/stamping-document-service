from flask import Flask
from config import Config
from eureka_client import define_eureka_client

def create_app():
    app = Flask(__name__)
    # define_eureka_client()
    from app.routes import main
    app.register_blueprint(main, url_prefix="/stamping")
    return app
