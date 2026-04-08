from fastapi import APIRouter, status
from pydantic import BaseModel
import uuid

router = APIRouter()


class IngestRequest(BaseModel):
    file_data: str
    mime_type: str
    source_type: str


class IngestResponse(BaseModel):
    task_id: str
    status: str


@router.post("/document", status_code=status.HTTP_202_ACCEPTED, response_model=IngestResponse)
def ingest_document(request: IngestRequest):
    return IngestResponse(task_id=str(uuid.uuid4()), status="pending_extraction")
