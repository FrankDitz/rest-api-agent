from fastapi import FastAPI, HTTPException
from app.schemas import AgentIngestPayload
from app.transform import normalize_agent_payload

app = FastAPI(title="Agent Data Normalizer API")

@app.get("/")
def root_msg():
    return {"message": "Welcome to the Agent Data Normalizer API. Use /health to check the status."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/agents")
def ingest_agent(payload: AgentIngestPayload):
    try:
        normalized = normalize_agent_payload(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    
    return {
        "message": "Payload normalized successfully",
        "normalized_data": normalized
    }