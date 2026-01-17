from dataclasses import dataclass
from typing import Optional, List


@dataclass(frozen=True)
class JobPosting:
    """A class representing a job posting entity."""
    id: str
    title: str
    description: str
    source_channel: str
    source_url: Optional[str] = None

@dataclass(frozen=True)
class JobPreference:
    """A class representing user job preferences."""
    required_keywords: List[str]
    excluded_keywords: List[str]
