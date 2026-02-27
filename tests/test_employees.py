"""
Tests for /api/v1/employees endpoints.
"""

SAMPLE_EMPLOYEE = {
    "first_name": "Alice",
    "last_name": "Smith",
    "gender": "Female",
    "date_of_birth": "1995-04-12",
    "department_id": 1,
}


def test_create_employee(client, auth_headers):
    resp = client.post("/api/v1/employees", json=SAMPLE_EMPLOYEE, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["employee"]["first_name"] == "Alice"


def test_list_employees(client, auth_headers):
    client.post("/api/v1/employees", json=SAMPLE_EMPLOYEE, headers=auth_headers)
    resp = client.get("/api/v1/employees", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()["count"] >= 1


def test_get_employee(client, auth_headers):
    create_resp = client.post(
        "/api/v1/employees", json=SAMPLE_EMPLOYEE, headers=auth_headers
    )
    emp_id = create_resp.get_json()["employee"]["id"]

    resp = client.get(f"/api/v1/employees/{emp_id}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.get_json()["employee"]["id"] == emp_id


def test_update_employee(client, auth_headers):
    create_resp = client.post(
        "/api/v1/employees", json=SAMPLE_EMPLOYEE, headers=auth_headers
    )
    emp_id = create_resp.get_json()["employee"]["id"]

    resp = client.put(
        f"/api/v1/employees/{emp_id}", json={"gender": "Male"}, headers=auth_headers
    )
    assert resp.status_code == 200
    assert resp.get_json()["employee"]["gender"] == "Male"


def test_delete_employee(client, auth_headers):
    create_resp = client.post(
        "/api/v1/employees", json=SAMPLE_EMPLOYEE, headers=auth_headers
    )
    emp_id = create_resp.get_json()["employee"]["id"]

    resp = client.delete(f"/api/v1/employees/{emp_id}", headers=auth_headers)
    assert resp.status_code == 200

    resp = client.get(f"/api/v1/employees/{emp_id}", headers=auth_headers)
    assert resp.status_code == 404


def test_employees_require_auth(client):
    resp = client.get("/api/v1/employees")
    assert resp.status_code == 401
