import os

HEADERS = {'Content-Type': 'application/json'}

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TmsDxTm53ViWecv9k6sCNuwS'
    TESTING = os.environ.get('TESTING') or False
    DEBUG = os.environ.get('DEBUG') or True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
