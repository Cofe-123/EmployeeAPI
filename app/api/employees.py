from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.emp_service import EmployeeService

employees_bp = Blueprint("employees", __name__)


# CREATE employee
@employees_bp.route("", methods=["POST"])
@jwt_required()
def create_employee():
    data = request.get_json()

    required_fields = [
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "department_id",
    ]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"message": "Invalid input"}), 400

    emp = EmployeeService.create(
        data["first_name"],
        data["last_name"],
        data["gender"],
        data["date_of_birth"],
        data["department_id"],
    )

    return jsonify({"employee": emp.__dict__}), 201


# GET all employees
@employees_bp.route("", methods=["GET"])
@jwt_required()
def get_employees():
    employees = EmployeeService.get_all()

    return (
        jsonify(
            {"count": len(employees), "employees": [e.__dict__ for e in employees]}
        ),
        200,
    )


# GET single employee
@employees_bp.route("/<int:emp_id>", methods=["GET"])
@jwt_required()
def get_employee(emp_id):
    emp = EmployeeService.get_by_id(emp_id)

    if not emp:
        return jsonify({"message": "Employee not found"}), 404

    return jsonify({"employee": emp.__dict__}), 200


# UPDATE employee
@employees_bp.route("/<int:emp_id>", methods=["PUT"])
@jwt_required()
def update_employee(emp_id):
    data = request.get_json()

    emp = EmployeeService.update(emp_id, data)

    if not emp:
        return jsonify({"message": "Employee not found"}), 404

    return jsonify({"employee": emp.__dict__}), 200


# DELETE employee
@employees_bp.route("/<int:emp_id>", methods=["DELETE"])
@jwt_required()
def delete_employee(emp_id):
    success = EmployeeService.delete(emp_id)

    if not success:
        return jsonify({"message": "Employee not found"}), 404

    return jsonify({"message": "Employee deleted"}), 200
