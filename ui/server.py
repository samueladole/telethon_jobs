from fastapi import FastAPI
from app.domain.entities import PendingApplication

app = FastAPI()
PENDING = {}

@app.get("/")
def list_pending():
    """List all pending applications."""
    return list(PENDING.values())

@app.post("/approve/{job_id}")
def approve(job_id: str):
    """Approve a pending application by job ID."""
    if job_id not in PENDING:
        return {"error": "Job ID not found."}
    if not AUTO_SUBMIT:
        PENDING[job.id] = PendingApplication(...)
        wait_for_approval(job.id)
    PENDING[job_id]["approved"] = True
