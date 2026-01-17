import yaml
from typing import Any, Dict

def load_config() -> Dict[str, Any]:
    """Loads configuration from a YAML file."""
    with open("config/settings.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)
