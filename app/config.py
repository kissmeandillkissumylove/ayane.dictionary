from pathlib import Path

BASE_DIR = Path(__file__).parent

# json files.
connect_json = "modules/json"

configuration_default = str(
	BASE_DIR / connect_json / "configuration_default.json")
configuration_patterns = str(
	BASE_DIR / connect_json / "configuration_patterns.json")

# txt files.
connect_txt = "modules/txt"

logs = str(
	BASE_DIR / connect_txt / "logs.log")

# constants.
LOG_SIZE_LIMIT = 1 * 1024 * 1024
NUM_LOG_FILES = 10
MAX_VALUE_LENGTH = 50
