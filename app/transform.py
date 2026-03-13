from typing import Any
from app.schemas import AgentIngestPayload


STATUS_MAP = {
    "enabled": "active",
    "active": "active",
    "running": "active",
    "disabled": "inactive",
    "inactive": "inactive",
    "paused": "inactive",
}

REGION_MAP = {
    "use1": "us-east-1",
    "usw2": "us-west-2",
}


def clean_string(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned = " ".join(value.strip().split())
    return cleaned or None


def normalize_status(value: str) -> str:
    cleaned = clean_string(value)
    if cleaned is None:
        raise ValueError("status cannot be empty")

    normalized = STATUS_MAP.get(cleaned.lower())
    if normalized is None:
        raise ValueError(f"unsupported status: {value}")

    return normalized


def normalize_region(value: str | None) -> str | None:
    cleaned = clean_string(value)
    if cleaned is None:
        return None

    lowered = cleaned.lower()
    return REGION_MAP.get(lowered, lowered)


def normalize_list(values: list[str] | None) -> list[str]:
    if not values:
        return []

    cleaned_items = []
    seen = set()

    for value in values:
        cleaned = clean_string(value)
        if cleaned is None:
            continue

        lowered = cleaned.lower()
        if lowered not in seen:
            seen.add(lowered)
            cleaned_items.append(lowered)

    return cleaned_items


def normalize_bool(value: str | None) -> bool | None:
    if value is None:
        return None

    cleaned = clean_string(value)
    if cleaned is None:
        return None

    lowered = cleaned.lower()

    if lowered in {"yes", "true", "1"}:
        return True
    if lowered in {"no", "false", "0"}:
        return False

    raise ValueError(f"unsupported boolean value: {value}")


def normalize_float(value: str | None) -> float | None:
    if value is None:
        return None

    cleaned = clean_string(value)
    if cleaned is None:
        return None

    return float(cleaned)


def normalize_int(value: str | None) -> int | None:
    if value is None:
        return None

    cleaned = clean_string(value)
    if cleaned is None:
        return None

    return int(cleaned)


def normalize_agent_payload(payload: AgentIngestPayload) -> dict[str, Any]:
    metrics = payload.metrics

    return {
        "agent_id": clean_string(payload.agentId).lower(),
        "name": clean_string(payload.displayName),
        "type": clean_string(payload.agentType).lower(),
        "team": clean_string(payload.teamName).title(),
        "owner_name": clean_string(payload.owner.name),
        "owner_email": payload.owner.email.strip().lower(),
        "status": normalize_status(payload.status),
        "channels": normalize_list(payload.channels),
        "region": normalize_region(payload.region),
        "created_at": payload.createdAt,
        "last_active_at": payload.lastActiveAt,
        "sla_tier": clean_string(payload.slaTier).lower() if payload.slaTier else None,
        "success_rate": normalize_float(metrics.successRate) if metrics else None,
        "avg_handle_time_ms": normalize_int(metrics.avgHandleTimeMs) if metrics else None,
        "monthly_ticket_volume": normalize_int(metrics.monthlyTicketVolume) if metrics else None,
        "capabilities": normalize_list(payload.capabilities),
        "contains_pii": normalize_bool(payload.containsPii),
        "escalation_email": payload.escalationEmail.strip().lower() if payload.escalationEmail else None,
        "notes": clean_string(payload.notes),
        "distribution_status": "pending",
    }