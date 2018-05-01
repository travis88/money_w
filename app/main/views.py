from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """Главная страница"""
    return render_template('index.html')