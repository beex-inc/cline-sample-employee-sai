from datetime import datetime
import re


class ValidationError(Exception):
    """カスタム検証エラー"""
    pass


def validate_employee_data(data, is_update=False):
    """
    社員データのバリデーション

    Args:
        data (dict): 検証する社員データ
        is_update (bool): 更新操作かどうか

    Raises:
        ValidationError: 検証エラーが発生した場合
    """
    errors = []

    # 更新時は全フィールドが必須ではない
    if not is_update:
        required_fields = ['employee_number', 'name',
                           'email', 'department', 'hire_date']
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f'{field}は必須項目です。')

    if 'employee_number' in data and data['employee_number']:
        if not re.match(r'^[A-Z0-9]{1,10}$', data['employee_number']):
            errors.append('社員番号は10文字以内の英大文字と数字で入力してください。')

    if 'email' in data and data['email']:
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            errors.append('有効なメールアドレスを入力してください。')

    if 'name' in data and data['name']:
        if len(data['name']) > 100:
            errors.append('氏名は100文字以内で入力してください。')

    if 'department' in data and data['department']:
        if len(data['department']) > 50:
            errors.append('部署は50文字以内で入力してください。')

    if 'hire_date' in data and data['hire_date']:
        try:
            datetime.strptime(data['hire_date'], '%Y-%m-%d')
        except ValueError:
            errors.append('入社日は YYYY-MM-DD 形式で入力してください。')

    if errors:
        raise ValidationError('\n'.join(errors))


def sanitize_input(data):
    """
    入力データのサニタイズ

    Args:
        data (dict): サニタイズする入力データ

    Returns:
        dict: サニタイズされたデータ
    """
    sanitized = {}
    for key, value in data.items():
        if isinstance(value, str):
            # 基本的なXSS対策
            value = value.replace('<', '&lt;').replace('>', '&gt;')
            # 前後の空白を削除
            value = value.strip()
        sanitized[key] = value
    return sanitized


def format_error_response(error):
    """
    エラーレスポンスのフォーマット

    Args:
        error: エラーオブジェクトまたはエラーメッセージ

    Returns:
        dict: フォーマットされたエラーレスポンス
    """
    if isinstance(error, ValidationError):
        return {'error': str(error)}
    elif isinstance(error, Exception):
        return {'error': f'エラーが発生しました: {str(error)}'}
    else:
        return {'error': str(error)}
