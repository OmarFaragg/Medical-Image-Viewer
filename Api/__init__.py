from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "dicom.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRETKEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, MedicalImage
    create_database(app)

    return app

def create_database(app):
    if not os.path.exists("Api/" + DB_NAME ):
        with app.app_context():
            db.create_all()
