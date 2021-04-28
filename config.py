import os

class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    Production configuration class
    """
    SQLALCHEMY_DATABASE_URI = "postgresql://uafyzmmvcusmlk:8e384a8b4a2aeb83b754ec59184d64504bf720cca1b49896747248f5e16695f2@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d9tfm57fdoaa1l?sslmode=require"


class DevConfig(Config):
    """
    Development configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/pitches'
    DEBUG = True
    
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/pitches_test'



config_options = {
    'production': ProdConfig,
    'development': DevConfig,
    'test':TestConfig
}
