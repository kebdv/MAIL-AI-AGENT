from sqlalchemy import Column, String, Text, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
import uuid
import datetime
from ..database import Base
import enum


class DraftStatus(str, enum.Enum):
    DRAFT = "Draft"
    APPROVED = "Approved"
    SENT = "Sent"
    REJECTED = "Rejected"


def generate_uuid():
    return str(uuid.uuid4())


class OutreachDraft(Base):
    __tablename__ = "outreach_drafts"
    id = Column(String, primary_key=True, default=generate_uuid)
    lead_id = Column(String, ForeignKey("leads.id"), nullable=False)
    subject_en = Column(String, nullable=False)
    body_en = Column(Text, nullable=False)
    subject_ar = Column(String, nullable=False)
    body_ar = Column(Text, nullable=False)
    prompt_template_used = Column(String, nullable=True)
    status = Column(Enum(DraftStatus), default=DraftStatus.DRAFT)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    lead = relationship("Lead", back_populates="drafts")
