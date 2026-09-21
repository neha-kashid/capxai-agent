from dataclasses import dataclass

from ai.capability_engine.evaluator import EvidenceEvaluation


@dataclass
class FollowUpQuestion:
    question_id: str
    capability_name: str
    question: str
    reason: str


class FollowUpGenerator:
    """Generate targeted follow-up questions when evidence is insufficient."""

    def generate(
        self,
        evaluation: EvidenceEvaluation,
    ) -> FollowUpQuestion | None:

        if not evaluation.needs_follow_up:
            return None

        capability = evaluation.capability_name

        question_templates = {
            "SQL": (
                "Can you explain your approach step by step and "
                "describe any edge cases you would consider?"
            ),
            "Python": (
                "Can you walk through a practical Python solution "
                "and explain why you chose that approach?"
            ),
            "PySpark": (
                "Can you explain how you would implement this in PySpark "
                "and how you would handle performance at scale?"
            ),
            "ETL/ELT": (
                "Can you describe how you would design this pipeline, "
                "including failure handling and data quality checks?"
            ),
            "BigQuery": (
                "Can you explain how you would optimize this BigQuery "
                "workload to improve performance and control cost?"
            ),
            "Airflow": (
                "Can you explain how you would design, monitor, "
                "and troubleshoot the Airflow DAG?"
            ),
        }

        question = question_templates.get(
            capability,
            (
                f"Can you provide a detailed practical example "
                f"demonstrating your {capability} capability?"
            ),
        )

        return FollowUpQuestion(
            question_id=f"{evaluation.question_id}-F1",
            capability_name=capability,
            question=question,
            reason=(
                f"Additional evidence is required for {capability} "
                f"because the initial response had insufficient evidence."
            ),
        )