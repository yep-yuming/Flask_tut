from flask import Flask


def create_app():
    app = Flask(__name__)
    #secret key!! dont share!
    app.config['SECRET_KEY'] = 'asdfbnujsa9u23yg9-788troweihnglv0923wy45 1320947190yrhbqw9suf3204'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefox = '/')
    app.register_blueprint(auth, url_prefox = '/')

    return app