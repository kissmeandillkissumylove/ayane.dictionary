from pathlib import Path

BASE_DIR = Path(__file__).parent

# json files.
connect_json = "modules/json"

configuration_default = str(
	BASE_DIR / connect_json / "configuration_default.json")

# txt files.
connect_txt = "modules/txt"

logs = str(
	BASE_DIR / connect_txt / "logs.log")
