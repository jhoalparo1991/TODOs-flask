from flask import Flask
from . import auth
from .views import app_route
from flask_bootstrap import Bootstrap5

from .config import Developmentconfig

def create_app():
        
    app = Flask(__name__)
        
    app.secret_key = Developmentconfig.SECRET_KEY
    
    app.config.from_object(Developmentconfig())
    
    Bootstrap5(app)
    
    app.register_blueprint(app_route)
    app.register_blueprint(auth.auth)

    return app
