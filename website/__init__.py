from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'core'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.init_app(app)#intialisimng the appp

    from .views import views
    from .auth import auth
   #registering the blueprints
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')

    return app

