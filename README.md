# AI Job Application Assistant
FastAPI backend for a fixed simulated analysis. The frontend is not implemented.

## Setup and run (PowerShell)

Run from the repository root. Python 3.13 is the inspected local version.
If needed, create the environment with `python -m venv backend/.venv`.

```powershell
.\backend\.venv\Scripts\python.exe -m pip install -r backend/requirements-dev.txt
.\backend\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Runtime dependencies: FastAPI (HTTP API), Pydantic (validation and schemas), and
Uvicorn (server). Development dependencies add pytest (tests) and HTTPX (FastAPI
test client). For runtime only, install `backend/requirements.txt` instead.

## API

POST `/api/analyses` with `Content-Type: application/json`:

```json
{
  "job_description": "Junior React and Python developer",
  "experience_profile": "Built a React project"
}
```

Both fields must be strings of 1–20,000 characters after trimming surrounding
whitespace. Missing, null, non-string, blank, oversized, or unexpected fields
return HTTP 422 using FastAPI's standard validation error format.

Every valid request returns HTTP 200 and this fixed payload:

```json
{
  "mode": "simulated",
  "notice": "This fixed example result does not assess the submitted text.",
  "analysis": {
    "summary": "Example only: a candidate could describe relevant project experience.",
    "suggestions": [
      "Describe a project and your contribution.",
      "Support statements about skills with concrete examples."
    ]
  }
}
```

`main.py` defines the route. FastAPI uses `schemas.py` to validate and trim the
request before the handler runs. The handler calls `analysis.py` without passing
submitted text. It returns the fixed result, which the response schema validates
before JSON serialization. Application code does not store text or call a model.

## Tests

```powershell
.\backend\.venv\Scripts\python.exe -m pytest backend/tests -q
```

Tests run in-process without a server. They cover fixed results for different
inputs, missing and unexpected fields, invalid types, blank values, malformed
JSON, and lengths 1, 19,999, 20,000, and 20,001 for each field. Padded boundary
inputs verify trimming occurs before size validation.
