from pydantic import BaseModel
from typing import List

class InterviewConfig(BaseModel):
    role_title: str
    job_description: str
    required_skills: List[str]
    experience_level: str
    interview_style: str = "conversational"
    max_duration_minutes: int = 30
    difficulty: str = "medium"

class InterviewResponse(BaseModel):
    question: str
    model_answer: str
    candidate_response: str = ""