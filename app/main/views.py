from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """Главная страница"""
    return 'hello world'