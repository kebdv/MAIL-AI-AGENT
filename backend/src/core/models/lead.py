from sqlalchemy import Column, String, Integer, JSON, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
import uuid
import datetime
from ..database import Base
import enum


class LeadStatus(str, enum.Enum):
    EXTRACTED = "Extracted"
    ENRICHED = "Enriched"
    QUALIFIED = "Qualified"
    CONTACTED = "Contacted"
    REPLIED = "Replied"
    FAILED = "Failed"


def generate_uuid():
    return str(uuid.uuid4())


class Company(Base):
    __tablename__ = "companies"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    domain = Column(String, unique=True, nullable=True)
    industry = Column(String, nullable=True)
    size = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    leads = relationship("Lead", back_populates="company")


class Lead(Base):
    __tablename__ = "leads"
    id = Column(String, primary_key=True, default=generate_uuid)
    company_id = Column(String, ForeignKey("companies.id"), nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=True)
    status = Column(Enum(LeadStatus), default=LeadStatus.EXTRACTED)
    score = Column(Integer, default=0)
    score_breakdown = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    company = relationship("Company", back_populates="leads")
    drafts = relationship("OutreachDraft", back_populates="lead")
    interactions = relationship("InteractionLog", back_populates="lead")
