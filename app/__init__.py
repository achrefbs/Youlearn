from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads


os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_IMAGES_DEST'] = 'app/static/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)




db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.init_app(app)

from app import routes, auth
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))