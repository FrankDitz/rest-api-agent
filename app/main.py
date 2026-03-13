from fastapi import FastAPI, HTTPException
from app.schemas import AgentIngestPayload
from app.transform import normalize_agent_payload
from app.database import Base, engine
from app import models
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.repository import save_agent

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agent Data Normalizer API")

@app.get("/")
def root_msg():
    return {"message": "Welcome to the Agent Data Normalizer API. Use /health to check the status."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/agents")
def ingest_agent(payload: AgentIngestPayload, db: Session = Depends(get_db)):
    try:
        normalized = normalize_agent_payload(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    saved_agent = save_agent(db, normalized)

    return {
        "message": "Agent stored successfully",
        "agent_id": saved_agent.agent_id,
        "distribution_status": saved_agent.distribution_status
    }