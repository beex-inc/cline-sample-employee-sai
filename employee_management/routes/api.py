from flask import Blueprint, request, jsonify
from models.employee import Employee, db
from utils.validation import validate_employee_data, sanitize_input, format_error_response

api = Blueprint('api', __name__)


@api.route('/employees', methods=['GET'])
def get_employees():
    """社員一覧を取得"""
    try:
        employees = Employee.query.all()
        return jsonify([emp.to_dict() for emp in employees])
    except Exception as e:
        return format_error_response(e), 500


@api.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    """特定の社員情報を取得"""
    try:
        employee = Employee.query.get_or_404(id)
        return jsonify(employee.to_dict())
    except Exception as e:
        return format_error_response(e), 404


@api.route('/employees', methods=['POST'])
def create_employee():
    """新規社員を登録"""
    try:
        data = request.get_json()
        sanitized_data = sanitize_input(data)
        validate_employee_data(sanitized_data)

        new_employee = Employee.create_from_dict(sanitized_data)
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({
            'message': '社員情報が正常に登録されました。',
            'employee': new_employee.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return format_error_response(e), 400


@api.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    """社員情報を更新"""
    try:
        employee = Employee.query.get_or_404(id)
        data = request.get_json()
        sanitized_data = sanitize_input(data)
        validate_employee_data(sanitized_data, is_update=True)

        employee.update_from_dict(sanitized_data)
        db.session.commit()

        return jsonify({
            'message': '社員情報が正常に更新されました。',
            'employee': employee.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return format_error_response(e), 400


@api.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    """社員情報を削除"""
    try:
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()

        return jsonify({
            'message': '社員情報が正常に削除されました。',
            'employee_id': id
        })
    except Exception as e:
        db.session.rollback()
        return format_error_response(e), 400
