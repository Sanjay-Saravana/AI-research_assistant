from fastapi import APIRouter
from app.models.schema import ResearchTopicRequest
from app.services.orchestrator import run_research

router = APIRouter()

@router.post("/research/")
async def research(request: ResearchTopicRequest):
    summary = run_research(request.topic)
    return {"summary": summary}