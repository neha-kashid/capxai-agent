from dataclasses import dataclass

from ai.capability_engine.assessment import AssessmentQuestion
from ai.capability_engine.responses import CandidateAnswer


@dataclass
class EvidenceEvaluation:
    question_id: str
    capability_name: str
    score: float
    confidence: str
    evidence: str
    needs_follow_up: bool


class MockEvaluator:
    """Temporary evaluator used for local development."""

    def evaluate(
        self,
        question: AssessmentQuestion,
        answer: CandidateAnswer,
    ) -> EvidenceEvaluation:

        answer_text = answer.answer.strip()

        if not answer_text:
            return EvidenceEvaluation(
                question_id=question.question_id,
                capability_name=question.capability_name,
                score=0,
                confidence="Low",
                evidence="No answer provided.",
                needs_follow_up=True,
            )

        word_count = len(answer_text.split())

        if word_count >= 40:
            score = 85
            confidence = "High"
            needs_follow_up = False
        elif word_count >= 20:
            score = 70
            confidence = "Medium"
            needs_follow_up = False
        else:
            score = 45
            confidence = "Low"
            needs_follow_up = True

        return EvidenceEvaluation(
            question_id=question.question_id,
            capability_name=question.capability_name,
            score=score,
            confidence=confidence,
            evidence=answer_text,
            needs_follow_up=needs_follow_up,
        )