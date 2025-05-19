# Technical Context

## 使用技術スタック

### バックエンド

- Python 3.9
- Flask (Web フレームワーク)
- SQLAlchemy (ORM)
- Flask-SQLAlchemy (Flask と SQLAlchemy の統合)
- Flask-CORS (CORS 対応)
- python-dotenv (環境変数管理)

### フロントエンド

- HTML/CSS
- JavaScript (Vanilla JS)
- jQuery
- Bootstrap 5 (UI フレームワーク)

### データベース

- MySQL 8.0
  - InnoDB エンジン
  - UTF-8mb4 文字セット

### 開発ツール

- Git (バージョン管理)
- Docker (コンテナ化)
- VSCode (推奨 IDE)

## 開発環境セットアップ

### 前提条件

```bash
# 必要なソフトウェア
- Python 3.9以上
- MySQL 8.0
- Docker (オプション)
```

### バックエンド環境構築

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env
# .envファイルを編集して必要な値を設定

# データベースの作成
mysql -u root -p
CREATE DATABASE employee_manager;

# 開発サーバーの起動
cd backend && python app.py
```

### Docker 環境

```bash
# 開発環境の起動
docker-compose up -d

# コンテナの確認
docker-compose ps

# ログの確認
docker-compose logs -f
```

## 依存関係

### バックエンド依存パッケージ

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
PyMySQL==1.1.0
python-dotenv==1.0.0
Werkzeug==3.0.1
SQLAlchemy==2.0.23
Flask-Migrate==4.0.5
Flask-CORS==4.0.0
cryptography==41.0.5
```

## 環境変数設定

```env
# Flask設定
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# データベース設定
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=employee_manager

# アプリケーション設定
DEBUG=True
```

## デプロイメント設定

### Docker Compose 設定

```yaml
version: "3.8"

services:
  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    ports:
      - "5000:5000"
    environment:
      - MYSQL_HOST=db
      - MYSQL_PORT=3306
      - MYSQL_USER=root
      - MYSQL_PASSWORD=root_password
      - MYSQL_DATABASE=employee_manager
      - FLASK_ENV=development
      - DEBUG=True
      - SECRET_KEY=your-secret-key-here
    depends_on:
      - db
    volumes:
      - ./backend:/app/backend

  frontend:
    build:
      context: .
      dockerfile: frontend/Dockerfile
    ports:
      - "80:80"
    depends_on:
      - backend
    volumes:
      - ./frontend:/usr/share/nginx/html

  db:
    image: mysql:8.0
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=root_password
      - MYSQL_DATABASE=employee_manager
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:

networks:
  app-network:
    driver: bridge
```

## 開発ガイドライン

### コーディング規約

1. Python

   - PEP 8 スタイルガイドに従う
   - Flake8 によるリンティング
   - Black によるフォーマット

2. JavaScript
   - ESLint の設定に従う
   - Prettier によるフォーマット

### ドキュメント規約

1. コードコメント

   - 日本語で記述
   - 関数やクラスには目的と使用方法を記載
   - 複雑なロジックには処理の説明を追加

2. API 仕様
   - エンドポイントの説明
   - リクエスト/レスポンスの形式
   - エラーケースの説明

### テスト規約

1. ユニットテスト

   - テストケースの命名規則
   - テストの独立性確保
   - モックの適切な使用

2. 統合テスト
   - API エンドポイントのテスト
   - データベース操作の検証
   - エラーケースの確認
