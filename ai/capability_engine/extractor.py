from ai.capability_engine.models import (
    Capability,
    CapabilityBlueprint,
    EvidenceItem,
    RequirementType,
)


class CapabilityExtractor:
    """Extract capabilities from a job description."""

    def extract(self, job_description: str) -> CapabilityBlueprint:
        raise NotImplementedError


class MockCapabilityExtractor(CapabilityExtractor):
    """Temporary extractor used for local development."""

    def extract(self, job_description: str) -> CapabilityBlueprint:
        capabilities = []

        jd = job_description.lower()

        if "sql" in jd:
            capabilities.append(
                Capability(
                    name="SQL",
                    category="Programming",
                    requirement=RequirementType.REQUIRED,
                    weight=25,
                    evidence_items=[
                        EvidenceItem(
                            "Query Writing",
                            "Can write correct SQL queries",
                        ),
                        EvidenceItem(
                            "Joins",
                            "Can correctly join multiple datasets",
                        ),
                        EvidenceItem(
                            "Optimization",
                            "Can improve inefficient SQL queries",
                        ),
                    ],
                )
            )

        if "python" in jd:
            capabilities.append(
                Capability(
                    name="Python",
                    category="Programming",
                    requirement=RequirementType.REQUIRED,
                    weight=20,
                    evidence_items=[
                        EvidenceItem(
                            "Problem Solving",
                            "Can solve programming problems",
                        ),
                        EvidenceItem(
                            "Data Processing",
                            "Can manipulate and transform data",
                        ),
                    ],
                )
            )

        if "pyspark" in jd or "spark" in jd:
            capabilities.append(
                Capability(
                    name="PySpark",
                    category="Distributed Processing",
                    requirement=RequirementType.REQUIRED,
                    weight=20,
                    evidence_items=[
                        EvidenceItem(
                            "DataFrame Operations",
                            "Can perform transformations and aggregations",
                        ),
                        EvidenceItem(
                            "Performance",
                            "Understands partitioning and shuffle",
                        ),
                    ],
                )
            )

        if "etl" in jd or "elt" in jd or "data pipeline" in jd:
            capabilities.append(
                Capability(
                    name="ETL/ELT",
                    category="Data Engineering",
                    requirement=RequirementType.REQUIRED,
                    weight=15,
                    evidence_items=[
                        EvidenceItem(
                            "Pipeline Design",
                            "Can design reliable data pipelines",
                        ),
                        EvidenceItem(
                            "Data Transformation",
                            "Can transform data between pipeline stages",
                        ),
                    ],
                )
            )

        if "bigquery" in jd:
            capabilities.append(
                Capability(
                    name="BigQuery",
                    category="Cloud & Data Platforms",
                    requirement=RequirementType.PREFERRED,
                    weight=10,
                    evidence_items=[
                        EvidenceItem(
                            "Query Design",
                            "Can write efficient BigQuery queries",
                        ),
                        EvidenceItem(
                            "Optimization",
                            "Understands partitioning and query cost optimization",
                        ),
                    ],
                )
            )

        if "airflow" in jd:
            capabilities.append(
                Capability(
                    name="Airflow",
                    category="Orchestration",
                    requirement=RequirementType.PREFERRED,
                    weight=10,
                    evidence_items=[
                        EvidenceItem(
                            "DAG Design",
                            "Can create and manage Airflow DAGs",
                        ),
                        EvidenceItem(
                            "Monitoring",
                            "Can monitor and troubleshoot pipeline failures",
                        ),
                    ],
                )
            )

        return CapabilityBlueprint(
            role_title="Data Engineer",
            capabilities=capabilities,
        )