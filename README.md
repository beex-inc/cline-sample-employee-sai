# 社員管理システム

## 概要
Flask/SQLAlchemyを利用した社員情報管理システム。
RESTful APIとWebインターフェースを提供し、社員データのCRUD操作を可能にします。

## 機能
- 社員情報の登録・照会・更新・削除
- データ検証と入力サニタイズ
- エラーハンドリング
- Web UIによる操作
- REST API

## 技術スタック
- Flask 2.3.2
- Flask-SQLAlchemy 3.0.3
- SQLite（開発環境）
- MySQL 8.0（Docker環境）

## システム要件
- Python 3.x
- Docker（オプション）

## セットアップ
### 1. 環境構築
```bash
git clone [repository-url]
cd employee-manager
pip install -r requirements.txt
```

### 2. データベース初期化
```bash
python run.py
```

### 3. Docker環境（オプション）
```bash
docker-compose up -d
```

## 使用方法
### アプリケーション起動
```bash
python run.py
```
サーバーは http://localhost:5002 で起動します。

### API エンドポイント
- GET /api/employees - 社員一覧取得
- GET /api/employees/<id> - 特定社員の情報取得
- POST /api/employees - 新規社員登録
- PUT /api/employees/<id> - 社員情報更新
- DELETE /api/employees/<id> - 社員情報削除

## プロジェクト構成
```
employee_management/
├── app.py              # アプリケーション設定
├── models/             # データモデル
├── routes/             # ルーティング
├── static/             # 静的ファイル
├── templates/          # テンプレート
└── utils/             # ユーティリティ
```

## 開発ガイドライン
- コードコメントは日本語で記述
- 変数名・関数名は英語で記述
- コミット前にコードレビューを実施

## データモデル
### 社員（Employee）
| フィールド | 型 | 説明 |
|------------|-------|------------|
| id | Integer | 主キー |
| employee_number | String(10) | 社員番号（一意） |
| name | String(100) | 氏名 |
| email | String(100) | メールアドレス（一意） |
| department | String(50) | 部署 |
| hire_date | Date | 入社日 |
| created_at | DateTime | 作成日時 |
| updated_at | DateTime | 更新日時 |

## エラーハンドリング
- 400: リクエストデータが不正
- 404: リソースが見つからない
- 500: サーバー内部エラー

## 開発環境のセットアップ
1. リポジトリのクローン
2. 依存パッケージのインストール
3. データベースの初期化
4. アプリケーションの起動

詳細な手順は上記のセットアップセクションを参照してください。

## 注意事項
- 本番環境での使用前にセキュリティ設定の見直しが必要です
- SECRET_KEYは必ず変更してください
- 本番環境ではSQLiteではなくMySQLの使用を推奨します
