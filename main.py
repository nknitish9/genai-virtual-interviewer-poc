from fastapi import FastAPI
from api.interview_routes import router as interview_router
from api.resume_routes import router as resume_router

app = FastAPI(title="GenAI Virtual Interviewer")

app.include_router(interview_router, prefix="/interview")
app.include_router(resume_router, prefix="/resume")

@app.get("/")
def root():
    return {"message": "Welcome to GenAI Virtual Interviewer!"}