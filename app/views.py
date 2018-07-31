from flask import Blueprint, render_template_string

blue = Blueprint('blue',__name__,url_prefix='/blue')

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/index/')
def index():
    return render_template_string('<h1>welcome,blue</h1>')