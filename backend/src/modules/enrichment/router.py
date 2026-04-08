from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EnrichRequest(BaseModel):
    lead_id: str


class ScoreBreakdown(BaseModel):
    industry: int
    email_validity: int


class EnrichResponse(BaseModel):
    lead_id: str
    status: str
    score: int
    score_breakdown: ScoreBreakdown


@router.post("", response_model=EnrichResponse)
def enrich_lead(request: EnrichRequest):
    return EnrichResponse(
        lead_id=request.lead_id,
        status="Enriched",
        score=85,
        score_breakdown=ScoreBreakdown(industry=30, email_validity=55),
    )
