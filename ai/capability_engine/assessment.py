from dataclasses import dataclass, field
from enum import Enum

from ai.capability_engine.models import CapabilityBlueprint


class QuestionType(Enum):
    MCQ = "mcq"
    CODING = "coding"
    SQL = "sql"
    SCENARIO = "scenario"
    SHORT_ANSWER = "short_answer"


@dataclass
class AssessmentQuestion:
    question_id: str
    question: str
    capability_name: str
    question_type: QuestionType
    difficulty: str
    max_score: float = 10.0


@dataclass
class Assessment:
    role_title: str
    questions: list[AssessmentQuestion] = field(default_factory=list)
    status: str = "draft"

    def activate(self) -> None:
        if not self.questions:
            raise ValueError(
                "Cannot activate an assessment without questions."
            )

        self.status = "active"


class AssessmentGenerator:
    """Generate a draft assessment from an approved capability blueprint."""

    def generate(
        self,
        blueprint: CapabilityBlueprint,
    ) -> Assessment:

        if blueprint.status.value != "approved":
            raise ValueError(
                "Only an approved blueprint can generate an assessment."
            )

        questions = []

        for index, capability in enumerate(
            blueprint.capabilities,
            start=1,
        ):
            questions.append(
                AssessmentQuestion(
                    question_id=f"Q{index}",
                    question=(
                        f"Demonstrate your practical knowledge of "
                        f"{capability.name}."
                    ),
                    capability_name=capability.name,
                    question_type=QuestionType.SCENARIO,
                    difficulty="medium",
                )
            )

        return Assessment(
            role_title=blueprint.role_title,
            questions=questions,
        )