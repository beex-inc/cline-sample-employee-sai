from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """メインページを表示"""
    return render_template('index.html')


@frontend.route('/form')
def form():
    """フォームページを表示（新規作成/編集用）"""
    return render_template('form.html')
