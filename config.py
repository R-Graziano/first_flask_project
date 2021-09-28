import os
from decouple import config

class Config(object):
    SECRET_KEY = config('SECRET_KEY')
    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_PORT =  config('MAIL_PORT')
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  os.environ.get('PASSWORD_EMAIL_APP') #os.environ.get('PASSWORD_EMAIL')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False