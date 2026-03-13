import json
from sqlalchemy.orm import Session
from app import models


def save_agent(db: Session, agent_data: dict):
    agent = models.Agent(
        agent_id=agent_data["agent_id"],
        name=agent_data["name"],
        type=agent_data["type"],
        team=agent_data["team"],
        owner_name=agent_data["owner_name"],
        owner_email=agent_data["owner_email"],
        status=agent_data["status"],
        channels=json.dumps(agent_data["channels"]),
        region=agent_data["region"],
        created_at=agent_data["created_at"],
        last_active_at=agent_data["last_active_at"],
        sla_tier=agent_data["sla_tier"],
        success_rate=agent_data["success_rate"],
        avg_handle_time_ms=agent_data["avg_handle_time_ms"],
        monthly_ticket_volume=agent_data["monthly_ticket_volume"],
        capabilities=json.dumps(agent_data["capabilities"]),
        contains_pii=agent_data["contains_pii"],
        escalation_email=agent_data["escalation_email"],
        notes=agent_data["notes"],
        distribution_status=agent_data["distribution_status"],
    )

    saved_agent = db.merge(agent)
    db.commit()
    db.refresh(saved_agent)

    return saved_agent