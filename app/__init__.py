from flask import Flask

from app.webhook.routes import webhook
from app.api.routes import api
from app.web.routes import web_app


# Creating our flask app
def create_app():

    app = Flask(__name__,template_folder='../templates',static_folder='../static',)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(api)
    app.register_blueprint(web_app)
    
    return app
