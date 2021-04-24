import os


class Config:
    """
    General configuration class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass


class ProdConfig(Config):
    """
    Production configuration class
    """
    pass


class DevConfig(Config):
    """
    Development configuration class
    """
    DEBUG = True


config_options = {
    'production': ProdConfig,
    'development': DevConfig
}
