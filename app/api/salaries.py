from flask import Blueprint, request, jsonify
from app.services.salary_service import SalaryService

salaries_bp = Blueprint("salaries", __name__)


@salaries_bp.route("/", methods=["POST"])
def create_salary():
    data = request.get_json()

    required_fields = [
        "employee_id",
        "basic_salary",
        "bonus",
        "allowances"
    ]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"message": "Invalid input"}), 400

    sal = SalaryService.create(
        data["employee_id"],
        data["basic_salary"],
        data["bonus"],
        data["allowances"]
    )

    return jsonify(sal.__dict__), 201


@salaries_bp.route("/", methods=["GET"])
def get_salaries():
    return jsonify([s.__dict__ for s in SalaryService.get_all()])