from dataclasses import dataclass, field

from ai.capability_engine.evaluator import EvidenceEvaluation
from ai.capability_engine.models import CapabilityBlueprint


@dataclass
class CapabilityResult:
    capability_name: str
    category: str
    requirement: str
    score: float
    confidence: str
    evidence: list[str] = field(default_factory=list)
    needs_evidence: bool = False


@dataclass
class CapabilityReport:
    candidate_id: str
    role_title: str
    results: list[CapabilityResult] = field(default_factory=list)

    def add_result(
        self,
        result: CapabilityResult,
    ) -> None:
        self.results.append(result)


class ReportGenerator:
    """Generate a capability report from assessment evidence."""

    def generate(
        self,
        candidate_id: str,
        blueprint: CapabilityBlueprint,
        evaluations: list[EvidenceEvaluation],
    ) -> CapabilityReport:

        report = CapabilityReport(
            candidate_id=candidate_id,
            role_title=blueprint.role_title,
        )

        for capability in blueprint.capabilities:

            capability_evaluations = [
                evaluation
                for evaluation in evaluations
                if evaluation.capability_name == capability.name
            ]

            if capability_evaluations:
                score = sum(
                    evaluation.score
                    for evaluation in capability_evaluations
                ) / len(capability_evaluations)

                confidence = self._calculate_confidence(
                    capability_evaluations
                )

                evidence = [
                    evaluation.evidence
                    for evaluation in capability_evaluations
                    if evaluation.evidence
                ]

                needs_evidence = any(
                    evaluation.needs_follow_up
                    for evaluation in capability_evaluations
                )

            else:
                score = 0
                confidence = "Low"
                evidence = []
                needs_evidence = True

            report.add_result(
                CapabilityResult(
                    capability_name=capability.name,
                    category=capability.category,
                    requirement=capability.requirement.value,
                    score=score,
                    confidence=confidence,
                    evidence=evidence,
                    needs_evidence=needs_evidence,
                )
            )

        return report

    def _calculate_confidence(
        self,
        evaluations: list[EvidenceEvaluation],
    ) -> str:

        confidence_levels = {
            "Low": 1,
            "Medium": 2,
            "High": 3,
        }

        average = sum(
            confidence_levels.get(
                evaluation.confidence,
                1,
            )
            for evaluation in evaluations
        ) / len(evaluations)

        if average >= 2.5:
            return "High"

        if average >= 1.5:
            return "Medium"

        return "Low"