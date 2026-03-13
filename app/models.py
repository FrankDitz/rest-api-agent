from sqlalchemy import Boolean, Column, Float, Integer, Text
from app.database import Base


class Agent(Base):
    __tablename__ = "agents"

    agent_id = Column(Text, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    type = Column(Text, nullable=False)
    team = Column(Text, nullable=False)
    owner_name = Column(Text, nullable=True)
    owner_email = Column(Text, nullable=False)
    status = Column(Text, nullable=False)
    channels = Column(Text, nullable=False)
    region = Column(Text, nullable=True)
    created_at = Column(Text, nullable=False)
    last_active_at = Column(Text, nullable=True)
    sla_tier = Column(Text, nullable=True)
    success_rate = Column(Float, nullable=True)
    avg_handle_time_ms = Column(Integer, nullable=True)
    monthly_ticket_volume = Column(Integer, nullable=True)
    capabilities = Column(Text, nullable=False)
    contains_pii = Column(Boolean, nullable=True)
    escalation_email = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    distribution_status = Column(Text, nullable=False)