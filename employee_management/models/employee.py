from datetime import datetime
from database import db


class Employee(db.Model):
    """
    社員情報モデル

    Attributes:
        id (int): 主キー
        employee_number (str): 社員番号（一意）
        name (str): 氏名
        email (str): メールアドレス（一意）
        department (str): 部署
        hire_date (date): 入社日
        created_at (datetime): 作成日時
        updated_at (datetime): 更新日時
    """
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    employee_number = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """
        モデルを辞書形式に変換

        Returns:
            dict: 社員情報の辞書
        """
        return {
            'id': self.id,
            'employee_number': self.employee_number,
            'name': self.name,
            'email': self.email,
            'department': self.department,
            'hire_date': self.hire_date.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def create_from_dict(data):
        """
        辞書データからEmployeeインスタンスを作成

        Args:
            data (dict): 社員情報データ

        Returns:
            Employee: 作成されたEmployeeインスタンス
        """
        return Employee(
            employee_number=data['employee_number'],
            name=data['name'],
            email=data['email'],
            department=data['department'],
            hire_date=datetime.strptime(data['hire_date'], '%Y-%m-%d').date()
        )

    def update_from_dict(self, data):
        """
        辞書データでインスタンスを更新

        Args:
            data (dict): 更新データ
        """
        if 'employee_number' in data:
            self.employee_number = data['employee_number']
        if 'name' in data:
            self.name = data['name']
        if 'email' in data:
            self.email = data['email']
        if 'department' in data:
            self.department = data['department']
        if 'hire_date' in data:
            self.hire_date = datetime.strptime(
                data['hire_date'], '%Y-%m-%d').date()
