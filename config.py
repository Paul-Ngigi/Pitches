import os


class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:root@localhost/pitches'
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
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True


config_options = {
    'production': ProdConfig,
    'development': DevConfig
}
