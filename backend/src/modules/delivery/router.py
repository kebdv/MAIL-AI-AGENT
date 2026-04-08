from fastapi import APIRouter, status
from pydantic import BaseModel
import uuid

router = APIRouter()


class DeliveryRequest(BaseModel):
    draft_id: str


class DeliveryResponse(BaseModel):
    interaction_log_id: str
    status: str


@router.post("/send", status_code=status.HTTP_202_ACCEPTED, response_model=DeliveryResponse)
def send_delivery(request: DeliveryRequest):
    return DeliveryResponse(interaction_log_id=str(uuid.uuid4()), status="queued_for_delivery")
