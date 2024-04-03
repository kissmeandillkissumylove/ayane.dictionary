from pathlib import Path

BASE_DIR = Path(__file__).parent

# JSON FILES.
CONNECT_JSON = "modules/files_json"
CONFIG_0 = BASE_DIR / CONNECT_JSON / "config_0.json"
CONFIG_PATTERNS = (
		BASE_DIR / CONNECT_JSON / "config_validation_patterns.json")

NOT_EMPTY_JSON = BASE_DIR / "tests/tests_files/not_empty.json"
EMPTY_JSON = BASE_DIR / "tests/tests_files/empty.json"
CORRECT_CONFIG = BASE_DIR / "tests/tests_files/correct_config.json"
INCORRECT_CONFIG = BASE_DIR / "tests/tests_files/incorrect_config.json"

# TXT FILES.
NOT_EMPTY_TXT = BASE_DIR / "tests/tests_files/not_empty.txt"
