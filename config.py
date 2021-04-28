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
    SQLALCHEMY_DATABASE_URI = 'postgresql://pykonncljnjurg:ca9419f42cf10926d49c52fd2a8e7b5e3c63b3d4d9b419d32a77c3b4d04c801c@ec2-18-214-140-149.compute-1.amazonaws.com:5432/dekiu1uqvid4ta?sslmode=require'


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
