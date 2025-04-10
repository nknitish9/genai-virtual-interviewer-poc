from pydantic import BaseModel

class EvaluationScores(BaseModel):
    recall: float
    precision: float
    f1_score: float

class FeedbackOutput(BaseModel):
    question: str
    scores: EvaluationScores