from enum import Enum

class ApplicationStatus(Enum):
    """Enumeration of application statuses."""
    NOT_SUPPORTED = "not_supported"
    DRY_RUN_SUCCESS = "dry_run_success"
    FAILED = "failed"
