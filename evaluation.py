def score_answer(candidate_answer: str, ideal_answer: str) -> dict:
    candidate_words = set(candidate_answer.lower().split())
    ideal_words = set(ideal_answer.lower().split())
    common = candidate_words & ideal_words
    recall = len(common) / len(ideal_words)
    precision = len(common) / len(candidate_words) if candidate_words else 0
    f1 = 2 * recall * precision / (recall + precision + 1e-6)
    return {"recall": recall, "precision": precision, "f1_score": f1}