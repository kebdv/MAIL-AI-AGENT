from sqlalchemy import Column, String, Text, DateTime
import uuid
import datetime
from ..database import Base


def generate_uuid():
    return str(uuid.uuid4())


class DeadLetter(Base):
    __tablename__ = "dead_letters"
    id = Column(String, primary_key=True, default=generate_uuid)
    task_name = Column(String, nullable=False)
    payload = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
