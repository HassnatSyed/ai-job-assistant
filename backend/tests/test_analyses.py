import pytest
from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)
VALID = {"job_description": "React and Python role", "experience_profile": "Built a React project"}
EXPECTED = {
    "mode": "simulated",
    "notice": "This fixed example result does not assess the submitted text.",
    "analysis": {
        "summary": "Example only: a candidate could describe relevant project experience.",
        "suggestions": [
            "Describe a project and your contribution.",
            "Support statements about skills with concrete examples.",
        ],
    },
}


@pytest.mark.parametrize("payload", [VALID, {"job_description": "Other job", "experience_profile": "Other experience"}])
def test_fixed_simulated_response(payload):
    response = client.post("/api/analyses", json=payload)
    assert response.status_code == 200
    assert response.json() == EXPECTED


@pytest.mark.parametrize("field", VALID)
@pytest.mark.parametrize("value", [None, 42, True, [], {}, "", "   ", "\t\n", "x" * 20001])
def test_invalid_field(field, value):
    response = client.post("/api/analyses", json={**VALID, field: value})
    assert response.status_code == 422


@pytest.mark.parametrize("field", VALID)
def test_missing_field(field):
    payload = dict(VALID)
    del payload[field]
    assert client.post("/api/analyses", json=payload).status_code == 422


@pytest.mark.parametrize("field", VALID)
@pytest.mark.parametrize("length", [1, 19999, 20000])
def test_trim_before_size_validation(field, length):
    response = client.post("/api/analyses", json={**VALID, field: " \n" + "x" * length + "\t "})
    assert response.status_code == 200
    assert response.json() == EXPECTED


def test_unexpected_field():
    assert client.post("/api/analyses", json={**VALID, "extra": "ignored?"}).status_code == 422


def test_malformed_json():
    response = client.post("/api/analyses", content="{", headers={"Content-Type": "application/json"})
    assert response.status_code == 422
