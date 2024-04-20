from injector import inject

from app.modules.base_structures import BaseContainer
from app.modules.config_validator import ConfigValidator
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
		self._save_button = None
		self._add_button = None
		self._find_button = None
		self._edit_button = None
		self._words_label = None

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
		self._set_save_button(config["save_button"])
		self._set_add_button(config["add_button"])
		self._set_find_button(config["find_button"])
		self._set_edit_button(config["edit_button"])
		self._set_words_label(config["words_label"])

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

