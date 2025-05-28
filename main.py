from flask import Flask
from models import db
from routes import routes





def createApp():

    app = Flask(__name__)

    app.secret_key = 'vanakam'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    db.init_app(app)
    app.register_blueprint(routes)



    return app
