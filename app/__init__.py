from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# from config import config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# db = SQLAlchemy()
bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()

def create_app(config_name='default'):

    # Cria o app flask
    app = Flask(__name__)

    # Inicia as configurações do app
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    # Inicia os módulos
    # db.init_app(app)
    bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)

    # Carregar os models
    # from . import models

    # Routes 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

