from pathlib import Path

BASE_DIR = Path(__file__).parent

# json files.
connect_json = "modules/json"

configuration_default = str(
	BASE_DIR / connect_json / "configuration_default.json")
