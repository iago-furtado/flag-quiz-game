# app/__init__.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models import Test
from config import Config
from app.database import db





def create_app():

    app = Flask(__name__)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.config.from_object(Config)

    db.init_app(app)
   

    return app
