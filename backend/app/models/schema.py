from pydantic import BaseModel

class ResearchTopicRequest(BaseModel):
    topic: str