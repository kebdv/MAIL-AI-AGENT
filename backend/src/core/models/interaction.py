from sqlalchemy import Column, String, JSON, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
import uuid
import datetime
from ..database import Base
import enum


class EventType(str, enum.Enum):
    SENT = "Sent"
    DELIVERED = "Delivered"
    OPENED = "Opened"
    REPLIED = "Replied"
    BOUNCED = "Bounced"


def generate_uuid():
    return str(uuid.uuid4())


class InteractionLog(Base):
    __tablename__ = "interaction_logs"
    id = Column(String, primary_key=True, default=generate_uuid)
    lead_id = Column(String, ForeignKey("leads.id"), nullable=False)
    event_type = Column(Enum(EventType), nullable=False)
    event_date = Column(DateTime, default=datetime.datetime.utcnow)
    metadata_json = Column(JSON, nullable=True)

    lead = relationship("Lead", back_populates="interactions")
