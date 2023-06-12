from flask import Flask
from . import auth
from .views import app_route
from flask_bootstrap import Bootstrap5
from .database import get_connection


from .config import Developmentconfig

db = get_connection()

print(db.get_database())
 
def create_app():
        
    app = Flask(__name__)
        
    app.secret_key = Developmentconfig.SECRET_KEY
    
    app.config.from_object(Developmentconfig())
    
    Bootstrap5(app)
    
    app.register_blueprint(app_route)
    app.register_blueprint(auth.auth)

    return app
