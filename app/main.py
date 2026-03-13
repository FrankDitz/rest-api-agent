from fastapi import FastAPI
from app.schemas import AgentIngestPayload

app = FastAPI(title="Agent Data Normalizer API")

@app.get("/")
def root_msg():
    return {"message": "Welcome to the Agent Data Normalizer API. Use /health to check the status."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/agents")
def ingest_agent(payload: AgentIngestPayload):
    return {
        "message": "Payload received successfully",
        "agent_id": payload.agentId
    }