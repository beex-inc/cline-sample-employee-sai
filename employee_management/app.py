from flask import Flask
from datetime import datetime
from database import db


def create_app():
    """
    アプリケーションファクトリー

    Returns:
        Flask: 設定済みのFlaskアプリケーション
    """
    app = Flask(__name__)

    # 設定の読み込み
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-here'

    # データベース初期化
    db.init_app(app)

    # Blueprintの登録
    from routes.api import api
    from routes.frontend import frontend
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(frontend)

    # データベース作成
    with app.app_context():
        db.create_all()

    return app


def main():
    """アプリケーション起動"""
    app = create_app()
    app.run(host='0.0.0.0', port=5002, debug=True)


if __name__ == '__main__':
    main()
