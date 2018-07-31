from flask import Flask
from app.api import init_api
from app.models import User      #识别model
from app.extentions import init_ext
from app.settings import envs
from app.views import init_blue


def create_app(env):
    app = Flask(__name__)
    #
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_blue(app)
    init_api(app)
    return app

