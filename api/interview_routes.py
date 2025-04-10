from fastapi import APIRouter, Body
from schemas.interview import InterviewConfig, InterviewResponse
from llm_implementation import LLaMAInterviewEngine

router = APIRouter()
interviewer = LLaMAInterviewEngine(model_path="models/llama/model.bin")

@router.post("/start")
def start_interview(config: InterviewConfig):
    # Mock interview start
    return {"message": f"Interview started for {config.role_title}"}

@router.post("/ask")
def ask_question(response: InterviewResponse):
    return {"follow_up": "Please elaborate on your experience with Python."}