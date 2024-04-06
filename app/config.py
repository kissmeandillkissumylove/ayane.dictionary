from pathlib import Path

BASE_DIR = Path(__file__).parent

# JSON FILES.
CONNECT_JSON = "modules/files_json"
CONFIG_0 = str(BASE_DIR / CONNECT_JSON / "config_0.json")
CONFIG_PATTERNS = str((
		BASE_DIR / CONNECT_JSON / "config_validation_patterns.json"))
OBJECTS_PLACES = str(
	BASE_DIR / CONNECT_JSON / "objects_places.json")

# JSON TEST FILES.
NOT_EMPTY_JSON = str(BASE_DIR / "tests/tests_files/not_empty.json")
EMPTY_JSON = str(BASE_DIR / "tests/tests_files/empty.json")
CORRECT_CONFIG = str(BASE_DIR / "tests/tests_files/correct_config.json")
INCORRECT_CONFIG = str(
	BASE_DIR / "tests/tests_files/incorrect_config.json")

# TXT FILES.
NOT_EMPTY_TXT = str(BASE_DIR / "tests/tests_files/not_empty.txt")

# ICO FILES.
TEST_ICON_ICO = str(BASE_DIR / "tests/tests_files/test_icon.ico")

# COLORS.
GRAY = "#B5B5B5"
BLACK = "#000000"
RED = "#DF1313"
WHITE = "#FFFFFF"
BLUE = "#2D81B2"
ALMOST_BLACK = "#19191A"
LIME = "#32CD32"
DARK_BLUE = "#2200AC"
DARK_GREEN = "#19732E"
GREEN = "#58BD66"

# FONT.
FONT = "verdana 8"
BOLD = " bold"

# TEXTS.
NEXT_BUTTON = "ɴᴇxᴛ"
SHOW_BUTTON = "sʜᴏᴡ"
RIGHT_BUTTON = "ʀɪɢʜᴛ"
WRONG_BUTTON = "ᴡʀᴏɴɢ"
AGAIN_BUTTON = "ᴀɢᴀɪɴ"
SAVE_BUTTON = "sᴀᴠᴇ"
MISTAKES_TEXT_LABEL = "ᴍɪsᴛᴀᴋᴇs:"
ADD_BUTTON = "ᴀᴅᴅ"
FIND_BUTTON = "ꜰɪɴᴅ"
EDIT_BUTTON = "ᴇᴅɪᴛ"
WORDS_LABEL = "ᴡᴏʀᴅs:"
