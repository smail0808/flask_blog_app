

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_admin import Admin






db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
admin = Admin()
# the function to redirect if we attemp to access login_required view
login_manager.login_view = 'users.login'
# customize message category if we attemp to access login_required view
login_manager.login_message_category = 'info'




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    from flaskblog.users.rootes import users
    from flaskblog.posts.rootes import posts
    from flaskblog.main.rootes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

