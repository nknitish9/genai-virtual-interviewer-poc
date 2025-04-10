from pydantic import BaseModel
from typing import List, Dict, Any

class CandidateInfo(BaseModel):
    name: str
    resume_id: str
    extracted_experience: List[Dict[str, Any]]
    extracted_education: List[Dict[str, Any]]
    extracted_skills: List[str]