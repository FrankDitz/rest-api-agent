from typing import List, Optional
from pydantic import BaseModel, EmailStr


class OwnerPayload(BaseModel):
    name: Optional[str] = None
    email: EmailStr


class MetricsPayload(BaseModel):
    successRate: Optional[str] = None
    avgHandleTimeMs: Optional[str] = None
    monthlyTicketVolume: Optional[str] = None


class AgentIngestPayload(BaseModel):
    agentId: str
    displayName: str
    agentType: str
    teamName: str
    owner: OwnerPayload
    status: str
    channels: Optional[List[str]] = None
    region: Optional[str] = None
    createdAt: str
    lastActiveAt: Optional[str] = None
    slaTier: Optional[str] = None
    metrics: Optional[MetricsPayload] = None
    capabilities: Optional[List[str]] = None
    containsPii: Optional[str] = None
    escalationEmail: Optional[EmailStr] = None
    notes: Optional[str] = None