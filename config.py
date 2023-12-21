import os


class Config(object):
    SECRET_KEY = 'ClassicCar'


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = '6000'
    SERVER_NAME = '127.0.0.1:5000'
    SQLALCHEMY_ENGINE = 'sqlite:///ClassicCar/ClassicCar.sqlite3'
