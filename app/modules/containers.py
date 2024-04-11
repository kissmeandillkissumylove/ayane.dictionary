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

	def set_config(self, config: dict):
		"""sets configuration values."""
		for key, value in config.items():
			if key == "root_window":
				self._set_root_window(value)
				continue

			if key == "screen_word_label":
				self._set_screen_word_label(value)
				continue

			if key == "screen_translation_label":
				self._set_screen_translation_label(value)
				continue

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
		return self._screen_word_label

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