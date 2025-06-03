from flask import Flask
from flask_login import LoginManager 
from routes import callRoutes
from models import db




def createApp():

    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)



    app.secret_key = 'vanakam'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    routes = callRoutes(app, login_manager)
    app.register_blueprint(routes)
    

    return app

def returnDb():
    return db


