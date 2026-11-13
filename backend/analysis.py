"""Fixed demonstration content; no model calls or storage."""

from backend.schemas import AnalysisContent, AnalysisResponse


def simulate_analysis() -> AnalysisResponse:
    return AnalysisResponse(
        mode="simulated",
        notice="This fixed example result does not assess the submitted text.",
        analysis=AnalysisContent(
            summary="Example only: a candidate could describe relevant project experience.",
            suggestions=[
                "Describe a project and your contribution.",
                "Support statements about skills with concrete examples.",
            ],
        ),
    )
