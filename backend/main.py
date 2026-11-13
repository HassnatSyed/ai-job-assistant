"""HTTP entry point for the simulated analysis API."""

from fastapi import FastAPI

from backend.analysis import simulate_analysis
from backend.schemas import AnalysisRequest, AnalysisResponse

app = FastAPI(title="AI Job Application Assistant")


@app.post("/api/analyses", response_model=AnalysisResponse)
def create_analysis(request: AnalysisRequest) -> AnalysisResponse:
    # Validation runs before this handler; the simulator needs no submitted text.
    return simulate_analysis()
