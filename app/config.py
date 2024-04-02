from pathlib import Path

BASE_DIR = Path(__file__).parent

# JSON FILES.
CONNECT_JSON = "modules/files_json"
CONFIG_0 = BASE_DIR / CONNECT_JSON / "config_0.json"
CONFIG_PATTERNS = (
		BASE_DIR / CONNECT_JSON / "config_validation_patterns.json")
