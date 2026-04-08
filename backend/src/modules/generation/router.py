from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter()


class GenerateRequest(BaseModel):
    lead_id: str
    prompt_template_id: str


class GenerateResponse(BaseModel):
    draft_id: str
    subject_en: str
    body_en: str
    subject_ar: str
    body_ar: str


@router.post("-draft", response_model=GenerateResponse)
def generate_draft(request: GenerateRequest):
    return GenerateResponse(
        draft_id=str(uuid.uuid4()),
        subject_en="Boosting TechFlow's Sales",
        body_en="...",
        subject_ar="تعزيز مبيعات TechFlow",
        body_ar="...",
    )
