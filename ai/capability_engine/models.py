from dataclasses import dataclass, field
from enum import Enum


class RequirementType(Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    NICE_TO_HAVE = "nice_to_have"


@dataclass
class EvidenceItem:
    name: str
    description: str


@dataclass
class Capability:
    name: str
    category: str
    requirement: RequirementType
    weight: float
    evidence_items: list[EvidenceItem] = field(default_factory=list)

class BlueprintStatus(Enum):
    DRAFT = "draft"
    APPROVED = "approved"

@dataclass
class CapabilityBlueprint:
    role_title: str
    capabilities: list[Capability] = field(default_factory=list)
    status: BlueprintStatus = BlueprintStatus.DRAFT

    def approve(self) -> None:
        self.status = BlueprintStatus.APPROVED
