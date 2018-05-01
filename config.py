import json


with open('config.json', 'r') as f:
    cfg = json.load(f)


class Config():
    """Базовая конфигурация"""
    SECRET_KEY = cfg['DEFAULT']['SECRET_KEY']
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        """Инициализация приложения"""
        pass


class DevelopmentConfig(Config):
    """Конфигурация для разработки"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = cfg['DEVELOPMENT']['DATABASE_URL']


class TestingConfig(Config):
    """Конфигурация для тестирования"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = cfg['TEST']['DATABASE_URL']
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Конфигурация для развёртывания"""
    SQLALCHEMY_DATABASE_URI = cfg['PRODUCTION']['DATABASE_URL']


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
