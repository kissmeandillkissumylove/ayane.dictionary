from pathlib import Path

BASE_DIR = Path(__file__).parent

# JSON FILES.
CONNECT_JSON = "modules/files_json"
CONFIG_0 = str(BASE_DIR / CONNECT_JSON / "config_0.json")
CONFIG_PATTERNS = str((
		BASE_DIR / CONNECT_JSON / "config_validation_patterns.json"))

NOT_EMPTY_JSON = str(BASE_DIR / "tests/tests_files/not_empty.json")
EMPTY_JSON = str(BASE_DIR / "tests/tests_files/empty.json")
CORRECT_CONFIG = str(BASE_DIR / "tests/tests_files/correct_config.json")
INCORRECT_CONFIG = str(
	BASE_DIR / "tests/tests_files/incorrect_config.json")

# TXT FILES.
NOT_EMPTY_TXT = str(BASE_DIR / "tests/tests_files/not_empty.txt")

# ICO FILES.
TEST_ICON_ICO = str(BASE_DIR / "tests/tests_files/test_icon.ico")
