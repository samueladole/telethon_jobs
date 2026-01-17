from dataclasses import dataclass

@dataclass(frozen=True)
class JobPreference:
    """Value object representing user job preferences."""
    required_keywords: list[str]
    excluded_keywords: list[str]
