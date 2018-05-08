import pathlib

basedir = pathlib.Path(__file__).parent.absolute()

class Config:
    SECRET_KEY = 'PARMONY'
    CARPARKS_PER_PAGE = 20
    TRANSACTIONS_PER_PAGE = 100

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(basedir/'data-dev.sqlite')

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(basedir/'data-test.sqlite')

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(basedir/'data-prod.sqlite')

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}

