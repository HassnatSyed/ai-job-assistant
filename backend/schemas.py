"""API schemas and trimmed, strict input validation."""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, StringConstraints

InputText = Annotated[
    str,
    StringConstraints(strict=True, strip_whitespace=True, min_length=1, max_length=20000),
]


class AnalysisRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_description: InputText
    experience_profile: InputText


class AnalysisContent(BaseModel):
    summary: str
    suggestions: list[str]


class AnalysisResponse(BaseModel):
    mode: Literal["simulated"]
    notice: str
    analysis: AnalysisContent
