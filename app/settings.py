import os


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


def get_db_uri(DATABASE):
    db = DATABASE.get('db','mysql')
    driver = DATABASE.get('driver','pymysql')
    user = DATABASE.get('user','root')
    password = DATABASE.get('password','1234')
    host = DATABASE.get('host','localhost')
    port = DATABASE.get('port','3306')
    name = DATABASE.get('name','flask_project_db')
    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,user,password,host,port,name)


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'db':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'1234',
        'host':'localhost',
        'port':'3306',
        'name':'flask_project_db'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestConfig(Config):
    TESTING = True
    DATABASE = {
        'db': 'mysql',
        'driver': 'pymysql',
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'name': 'flask_project_db'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        'db': 'mysql',
        'driver': 'pymysql',
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'name': 'flask_project_db'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop':DevelopConfig,
    'testing':TestConfig,
    'staging':StagingConfig,
    'default':DevelopConfig

}
