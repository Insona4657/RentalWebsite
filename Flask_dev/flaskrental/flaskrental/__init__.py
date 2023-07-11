import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskrental.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskrental.rentalusers.routes import rentalusers
    from flaskrental.products.routes import products
    from flaskrental.main.routes import main
    from flaskrental.errors.handlers import errors
    app.register_blueprint(rentalusers)
    app.register_blueprint(products)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    with app.app_context():
        db.create_all()

    return(app)
