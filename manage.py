import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


app = create_app(os.getenv('MONEY_W_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """Создаёт контекст для командной строки"""
    return dict(app=app, db=db)


# добавляем команды управления приложением для терминала
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__' :
    manager.run()
