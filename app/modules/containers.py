from injector import inject

from app.config import database
from app.modules.base_structures import BaseContainer
from app.modules.config_validator import ConfigValidator
from app.modules.file_readers import JsonFileReader
from app.modules.logger import CustomLogger


class ConfigContainer(BaseContainer):
	"""contains configuration dictionaries."""

	@inject
	def __init__(self, validator: ConfigValidator, logger: CustomLogger):
		"""ConfigContainer __init__."""
		if isinstance(logger, CustomLogger):
			self._logger = logger
			self._logger.log_debug("set: _logger", self._logger)
		else:
			raise TypeError("wrong type for the logger.")

		self._config_validator = validator
		self._logger.log_debug(
			"set: _config_validator", self._config_validator)

		self._root_window = None
		self._screen_word_label = None
		self._screen_translation_label = None
		self._next_button = None
		self._show_button = None
		self._right_button = None
		self._wrong_button = None
		self._again_button = None
		self._add_button = None
		self._find_button = None
		self._edit_button = None
		self._remove_button = None
		self._save_button = None
		self._words_label = None
		self._words_counter_label = None
		self._mistakes_label = None
		self._mistakes_counter_label = None
		self._word_label = None
		self._word_text = None
		self._transcription_label = None
		self._transcription_text = None
		self._part_of_speech_label = None
		self._part_of_speech_text = None
		self._usage_example_label = None
		self._usage_example_text = None
		self._translation_label = None
		self._translation_text = None
		self._result_label = None
		self._command_label = None

	def set_config(self, config: dict):
		"""sets configuration values."""
		self._set_root_window(config["root_window"])
		self._set_screen_word_label(config["screen_word_label"])
		self._set_screen_translation_label(
			config["screen_translation_label"])
		self._set_next_button(config["next_button"])
		self._set_show_button(config["show_button"])
		self._set_right_button(config["right_button"])
		self._set_wrong_button(config["wrong_button"])
		self._set_again_button(config["again_button"])
		self._set_add_button(config["add_button"])
		self._set_find_button(config["find_button"])
		self._set_edit_button(config["edit_button"])
		self._set_remove_button(config["remove_button"])
		self._set_save_button(config["save_button"])
		self._set_words_label(config["words_label"])
		self._set_words_counter_label(config["words_counter_label"])
		self._set_mistakes_label(config["mistakes_label"])
		self._set_mistakes_counter_label(config["mistakes_counter_label"])
		self._set_word_label(config["word_label"])
		self._set_word_text(config["word_text"])
		self._set_transcription_label(config["transcription_label"])
		self._set_transcription_text(config["transcription_text"])
		self._set_part_of_speech_label(config["part_of_speech_label"])
		self._set_part_of_speech_text(config["part_of_speech_text"])
		self._set_usage_example_label(config["usage_example_label"])
		self._set_usage_example_text(config["usage_example_text"])
		self._set_translation_label(config["translation_label"])
		self._set_translation_text(config["translation_text"])
		self._set_result_label(config["result_label"])
		self._set_command_label(config["command_label"])

	@property
	def root_window(self) -> dict:
		"""returns _root_window."""
		return self._root_window

	def _set_root_window(self, config: dict):
		"""sets a new value for the _root_window."""
		if self._config_validator.validate(config, "root"):
			self._root_window = config
			self._logger.log_debug(
				"set: _root_window", self._root_window)
		else:
			self._logger.log_warning(
				"try: _root_window", config)

	@property
	def screen_word_label(self) -> dict:
		"""returns _screen_word_label."""
		return self._screen_word_label

	def _set_screen_word_label(self, config: dict):
		"""sets a new value for the _screen_word_label."""
		if self._config_validator.validate(config, "label"):
			self._screen_word_label = config
			self._logger.log_debug(
				"set: _screen_word_label", self._screen_word_label)
		else:
			self._logger.log_warning(
				"try: _screen_word_label", config)

	@property
	def screen_translation_label(self) -> dict:
		"""returns _screen_translation_label."""
		return self._screen_translation_label

	def _set_screen_translation_label(self, config: dict):
		"""sets a new value for the _screen_translation_label."""
		if self._config_validator.validate(config, "label"):
			self._screen_translation_label = config
			self._logger.log_debug(
				"set: _screen_translation_label",
				self._screen_translation_label)
		else:
			self._logger.log_warning(
				"try: _screen_translation_label", config)

	@property
	def next_button(self) -> dict:
		"""returns _next_button."""
		return self._next_button

	def _set_next_button(self, config: dict):
		"""sets a new value for the _next_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._next_button = config
			self._logger.log_debug(
				"set: _next_button", self._next_button)
		else:
			self._logger.log_warning("try: _next_button", config)

	@property
	def show_button(self) -> dict:
		"""returns _show_button."""
		return self._show_button

	def _set_show_button(self, config: dict):
		"""sets a new value for the _show_button."""
		if self._config_validator.validate(config, "button", "disabled"):
			self._show_button = config
			self._logger.log_debug(
				"set: _show_button", self._show_button)
		else:
			self._logger.log_warning("try: _show_button", config)

	@property
	def right_button(self) -> dict:
		"""returns _right_button."""
		return self._right_button

	def _set_right_button(self, config: dict):
		"""sets a new value for the _right_button."""
		if self._config_validator.validate(config, "button", "disabled"):
			self._right_button = config
			self._logger.log_debug(
				"set: _right_button", self._right_button)
		else:
			self._logger.log_warning("try: _right_button", config)

	@property
	def wrong_button(self) -> dict:
		"""returns _wrong_button."""
		return self._wrong_button

	def _set_wrong_button(self, config: dict):
		"""sets a new value for the _wrong_button."""
		if self._config_validator.validate(config, "button", "disabled"):
			self._wrong_button = config
			self._logger.log_debug(
				"set: _wrong_button", self._wrong_button)
		else:
			self._logger.log_warning("try: _wrong_button", config)

	@property
	def again_button(self) -> dict:
		"""returns _again_button."""
		return self._again_button

	def _set_again_button(self, config: dict):
		"""sets a new value for the _again_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._again_button = config
			self._logger.log_debug(
				"set: _again_button", self._again_button)
		else:
			self._logger.log_warning("try: _again_button", config)

	@property
	def add_button(self) -> dict:
		"""returns _add_button."""
		return self._add_button

	def _set_add_button(self, config: dict):
		"""sets a new value for the _add_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._add_button = config
			self._logger.log_debug(
				"set: _add_button", self._add_button)
		else:
			self._logger.log_warning("try: _add_button", config)

	@property
	def find_button(self) -> dict:
		"""returns _find_button."""
		return self._find_button

	def _set_find_button(self, config: dict):
		"""sets a new value for the _find_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._find_button = config
			self._logger.log_debug(
				"set: _find_button", self._find_button)
		else:
			self._logger.log_warning("try: _find_button", config)

	@property
	def edit_button(self) -> dict:
		"""returns _edit_button."""
		return self._edit_button

	def _set_edit_button(self, config: dict):
		"""sets a new value for the _edit_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._edit_button = config
			self._logger.log_debug(
				"set: _edit_button", self._edit_button)
		else:
			self._logger.log_warning("try: _edit_button", config)

	@property
	def remove_button(self) -> dict:
		"""returns _remove_button."""
		return self._remove_button

	def _set_remove_button(self, config: dict):
		"""sets a new value for the _remove_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._remove_button = config
			self._logger.log_debug(
				"set: _remove_button", self._remove_button)
		else:
			self._logger.log_warning("try: _remove_button", config)

	@property
	def save_button(self) -> dict:
		"""returns _save_button."""
		return self._save_button

	def _set_save_button(self, config: dict):
		"""sets a new value for the _save_button."""
		if self._config_validator.validate(config, "button", "normal"):
			self._save_button = config
			self._logger.log_debug(
				"set: _save_button", self._save_button)
		else:
			self._logger.log_warning("try: _save_button", config)

	@property
	def words_label(self) -> dict:
		"""returns _words_label."""
		return self._words_label

	def _set_words_label(self, config: dict):
		"""sets a new value for the _words_label."""
		if self._config_validator.validate(config, "label"):
			self._words_label = config
			self._logger.log_debug(
				"set: _words_label", self._words_label)
		else:
			self._logger.log_warning("try: _words_label", config)

	@property
	def words_counter_label(self) -> dict:
		"""returns _words_counter_label."""
		return self._words_counter_label

	def _set_words_counter_label(self, config: dict):
		"""sets a new value for the _words_counter_label."""
		if self._config_validator.validate(config, "label"):
			self._words_counter_label = config
			self._logger.log_debug(
				"set: _words_counter_label", self._words_counter_label)
		else:
			self._logger.log_warning(
				"try: _words_counter_label", config)

	@property
	def mistakes_label(self) -> dict:
		"""returns _mistakes_label."""
		return self._mistakes_label

	def _set_mistakes_label(self, config: dict):
		"""sets a new value for the _mistakes_label."""
		if self._config_validator.validate(config, "label"):
			self._mistakes_label = config
			self._logger.log_debug(
				"set: _mistakes_label", self._mistakes_label)
		else:
			self._logger.log_warning("try: _mistakes_label", config)

	@property
	def mistakes_counter_label(self) -> dict:
		"""returns _mistakes_counter_label."""
		return self._mistakes_counter_label

	def _set_mistakes_counter_label(self, config: dict):
		"""sets a new value for the _mistakes_counter_label."""
		if self._config_validator.validate(config, "label"):
			self._mistakes_counter_label = config
			self._logger.log_debug(
				"set: _mistakes_counter_label",
				self._mistakes_counter_label)
		else:
			self._logger.log_warning(
				"try: _mistakes_counter_label", config)

	@property
	def word_label(self) -> dict:
		"""returns _word_label."""
		return self._word_label

	def _set_word_label(self, config: dict):
		"""sets a new value for the _word_label."""
		if self._config_validator.validate(config, "label"):
			self._word_label = config
			self._logger.log_debug(
				"set: _word_label", self._word_label)
		else:
			self._logger.log_warning("try: _word_label", config)

	@property
	def word_text(self) -> dict:
		"""returns _word_text."""
		return self._word_text

	def _set_word_text(self, config: dict):
		"""sets a new value for the _word_text."""
		if self._config_validator.validate(config, "text"):
			self._word_text = config
			self._logger.log_debug(
				"set: _word_text", self._word_text)
		else:
			self._logger.log_warning("try: _word_text", config)

	@property
	def transcription_label(self) -> dict:
		"""returns _transcription_label."""
		return self._transcription_label

	def _set_transcription_label(self, config: dict):
		"""sets a new value for the _transcription_label."""
		if self._config_validator.validate(config, "label"):
			self._transcription_label = config
			self._logger.log_debug(
				"set: _transcription_label", self._transcription_label)
		else:
			self._logger.log_warning("try: _transcription_label", config)

	@property
	def transcription_text(self) -> dict:
		"""returns _transcription_text."""
		return self._transcription_text

	def _set_transcription_text(self, config: dict):
		"""sets a new value for the _transcription_text."""
		if self._config_validator.validate(config, "text"):
			self._transcription_text = config
			self._logger.log_debug(
				"set: _transcription_text", self._transcription_text)
		else:
			self._logger.log_warning("try: _transcription_text", config)

	@property
	def part_of_speech_label(self) -> dict:
		"""returns _part_of_speech_label."""
		return self._part_of_speech_label

	def _set_part_of_speech_label(self, config: dict):
		"""sets a new value for the _part_of_speech_label."""
		if self._config_validator.validate(config, "label"):
			self._part_of_speech_label = config
			self._logger.log_debug(
				"set: _part_of_speech_label", self._part_of_speech_label)
		else:
			self._logger.log_warning("try: _part_of_speech_label", config)

	@property
	def part_of_speech_text(self) -> dict:
		"""returns _part_of_speech_text."""
		return self._part_of_speech_text

	def _set_part_of_speech_text(self, config: dict):
		"""sets a new value for the _part_of_speech_text."""
		if self._config_validator.validate(config, "text"):
			self._part_of_speech_text = config
			self._logger.log_debug(
				"set: _part_of_speech_text", self._part_of_speech_text)
		else:
			self._logger.log_warning("try: _part_of_speech_text", config)

	@property
	def usage_example_label(self) -> dict:
		"""returns _usage_example_label."""
		return self._usage_example_label

	def _set_usage_example_label(self, config: dict):
		"""sets a new value for the _usage_example_label."""
		if self._config_validator.validate(config, "label"):
			self._usage_example_label = config
			self._logger.log_debug(
				"set: _usage_example_label", self._usage_example_label)
		else:
			self._logger.log_warning("try: _usage_example_label", config)

	@property
	def usage_example_text(self) -> dict:
		"""returns _usage_example_text."""
		return self._usage_example_text

	def _set_usage_example_text(self, config: dict):
		"""sets a new value for the _usage_example_text."""
		if self._config_validator.validate(config, "text"):
			self._usage_example_text = config
			self._logger.log_debug(
				"set: _usage_example_text", self._usage_example_text)
		else:
			self._logger.log_warning("try: _part_of_speech_text", config)

	@property
	def translation_label(self) -> dict:
		"""returns _translation_label."""
		return self._translation_label

	def _set_translation_label(self, config: dict):
		"""sets a new value for the _translation_label."""
		if self._config_validator.validate(config, "label"):
			self._translation_label = config
			self._logger.log_debug(
				"set: _translation_label", self._translation_label)
		else:
			self._logger.log_warning("try: _translation_label", config)

	@property
	def translation_text(self) -> dict:
		"""returns _translation_text."""
		return self._translation_text

	def _set_translation_text(self, config: dict):
		"""sets a new value for the _translation_text."""
		if self._config_validator.validate(config, "text"):
			self._translation_text = config
			self._logger.log_debug(
				"set: _translation_text", self._translation_text)
		else:
			self._logger.log_warning("try: _translation_text", config)

	@property
	def result_label(self) -> dict:
		"""returns _result_label."""
		return self._result_label

	def _set_result_label(self, config: dict):
		"""sets a new value for the _result_label."""
		if self._config_validator.validate(config, "label"):
			self._result_label = config
			self._logger.log_debug(
				"set: _result_label", self._result_label)
		else:
			self._logger.log_warning("try: _result_label", config)

	@property
	def command_label(self) -> dict:
		"""returns _command_label."""
		return self._command_label

	def _set_command_label(self, config: dict):
		"""sets a new value for the _command_label."""
		if self._config_validator.validate(config, "label"):
			self._command_label = config
			self._logger.log_debug(
				"set: _command_label", self._command_label)
		else:
			self._logger.log_warning("try: _command_label", config)


class DictionaryContainer(BaseContainer):
	"""contains dictionary."""

	@inject
	def __init__(
			self,
			logger: CustomLogger,
			file_reader: JsonFileReader):
		"""DictionaryContainer __init__."""
		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong type for the logger.")
		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

		if not isinstance(file_reader, JsonFileReader):
			raise TypeError("wrong type for the file reader.")
		self._file_reader = file_reader
		self._logger.log_debug("set: _file_reader", self._file_reader)

		self._dictionary = None
		self._logger.log_debug("set: _dictionary", self._dictionary)

	def preload_dictionary(self, path=database):
		"""load all the words."""
		self._dictionary = self._file_reader.read_(path)
		self._logger.log_debug("set: _dictionary", self._dictionary)

		self._sort_by_priority()

	def _sort_by_priority(self):
		"""sorts all the words by priority."""
		self._logger.log_debug("run: _sort_by_priority()")

		if self._dictionary is not None:
			self._sorted_dictionary = sorted(
				self._dictionary.items(), key=lambda x: x[1][-1])
		else:
			self._sorted_dictionary = None

	@property
	def sorted_dictionary(self) -> list:
		"""returns _sorted_dictionary."""
		return self._sorted_dictionary

	@property
	def dictionary(self):
		"""returns _dictionary."""
		return self._dictionary
