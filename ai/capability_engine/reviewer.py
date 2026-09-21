from ai.capability_engine.models import (
    Capability,
    CapabilityBlueprint,
    RequirementType,
)


class BlueprintReviewer:
    """Review and modify a capability blueprint before approval."""

    def update_requirement(
        self,
        capability: Capability,
        requirement: RequirementType,
    ) -> None:
        capability.requirement = requirement

    def update_weight(
        self,
        capability: Capability,
        weight: float,
    ) -> None:
        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        capability.weight = weight

    def approve(
        self,
        blueprint: CapabilityBlueprint,
    ) -> None:
        if not blueprint.capabilities:
            raise ValueError(
                "Cannot approve a blueprint without capabilities."
            )

        total_weight = sum(
            capability.weight
            for capability in blueprint.capabilities
        )

        if total_weight <= 0:
            raise ValueError(
                "Total capability weight must be greater than zero."
            )

        blueprint.approve()