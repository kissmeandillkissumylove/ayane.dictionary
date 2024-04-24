from pathlib import Path

BASE_DIR = Path(__file__).parent

# json files.
connect_json = "modules/json"

configuration_default = str(
	BASE_DIR / connect_json / "configuration_default.json")
configuration_patterns = str(
	BASE_DIR / connect_json / "configuration_patterns.json")
database = str(
	BASE_DIR / connect_json / "database.json")

# txt files.
connect_txt = "modules/txt"

logs = str(
	BASE_DIR / connect_txt / "logs.log")

# constants.
LOG_SIZE_LIMIT = 1 * 1024 * 1024
NUM_LOG_FILES = 10
MAX_VALUE_LENGTH = 50
PREPARE_NEW_DICTIONARY = (
	"\ta new list of words has been prepared.")
WORD_EXISTS = "this word is already in the dictionary."
INDENT_MESSAGE = "don't use indentation in the fields. (enter, '\\n')"
BOTH_FIELDS_EMPTY = "the word and translation fields are too short."
WORD_FIELD_EMPTY = "the word field is too short."
TRANSL_FIELD_EMPTY = "the translation field is too short."
WORD_ADDED = "the new word added successfully."
NO_SUCH_WORD = "there is no such word in the dictionary."
EDITED = "word parameters have been edited."
