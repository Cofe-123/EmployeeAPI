from flask import Blueprint, request, jsonify
from app.services.emp_service import EmployeeService

employees_bp = Blueprint("employees", __name__)


@employees_bp.route("/", methods=["POST"])
def create_employee():
    data = request.get_json()

    required_fields = [
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "department_id"
    ]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"message": "Invalid input"}), 400

    emp = EmployeeService.create(
        data["first_name"],
        data["last_name"],
        data["gender"],
        data["date_of_birth"],
        data["department_id"]
    )

    return jsonify(emp.__dict__), 201


@employees_bp.route("/", methods=["GET"])
def get_employees():
    return jsonify([e.__dict__ for e in EmployeeService.get_all()])