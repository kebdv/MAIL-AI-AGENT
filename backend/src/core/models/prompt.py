from sqlalchemy import Column, String, Text, Boolean, DateTime
import uuid
import datetime
from ..database import Base


def generate_uuid():
    return str(uuid.uuid4())


class SystemPrompt(Base):
    __tablename__ = "system_prompts"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, unique=True, nullable=False)
    content_english_logic = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
