import os

class Config(object):
    SECRET_KEY = 'my_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT =  465 #587
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  os.environ.get('PASSWORD_EMAIL_APP') #os.environ.get('PASSWORD_EMAIL')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysqlroot@localhost/flask' # Sin password: 'mysql://root:@localhost/flask' con password: 'mysql://root:password@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
