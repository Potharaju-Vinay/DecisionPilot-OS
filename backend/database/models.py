from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Float, Text


class Base(DeclarativeBase):
    pass


class Decision(Base):

    __tablename__ = "decisions"

    workflow_id = Column(String, primary_key=True)

    recommendation = Column(Text)

    confidence = Column(Float)

    approval_status = Column(String)


class WorkflowMemory(Base):

    __tablename__ = "workflow_memory"

    workflow_id = Column(String, primary_key=True)

    customer = Column(String)

    query = Column(Text)

    document_source = Column(String)

    fingerprint = Column(String)

    decision = Column(Text)

    recommendation = Column(Text)

    explanation = Column(Text)

    business_score = Column(Float)

    risk_score = Column(Float)

    confidence = Column(Float)

    created_at = Column(String)