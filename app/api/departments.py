from flask import Blueprint, request, jsonify
from app.services.dept_service import DepartmentService

departments_bp = Blueprint("departments", __name__)


@departments_bp.route("/", methods=["POST"])
def create_department():
    data = request.get_json()

    if not data or "department_name" not in data or "location" not in data:
        return jsonify({"message": "Invalid input"}), 400

    dept = DepartmentService.create(data["department_name"], data["location"])

    return jsonify(dept.__dict__), 201


@departments_bp.route("/", methods=["GET"])
def get_departments():
    return jsonify([d.__dict__ for d in DepartmentService.get_all()])
