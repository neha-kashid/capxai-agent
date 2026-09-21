from dataclasses import dataclass, field


@dataclass
class CandidateAnswer:
    question_id: str
    answer: str


@dataclass
class CandidateSubmission:
    candidate_id: str
    assessment_id: str
    answers: list[CandidateAnswer] = field(default_factory=list)

    def add_answer(
        self,
        question_id: str,
        answer: str,
    ) -> None:
        if not answer.strip():
            raise ValueError("Answer cannot be empty.")

        self.answers.append(
            CandidateAnswer(
                question_id=question_id,
                answer=answer,
            )
        )