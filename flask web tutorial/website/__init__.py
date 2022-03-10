from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    #creating flask app
    app = Flask(__name__)
    #secret key!! dont share!
    app.config['SECRET_KEY'] = 'asdfbnujsa9u23yg9-788'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefox = '/')
    app.register_blueprint(auth, url_prefox = '/')

    from .models import User,Note

    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('Created Database!')