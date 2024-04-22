"""contains config container and config validator."""
import re

from injector import inject

from app.config import configuration_patterns
from app.modules.base_structures import BaseValidator
from app.modules.file_readers import JsonFileReader
from app.modules.logger import CustomLogger


class ConfigValidator(BaseValidator):
	"""validator for file config parts."""

	@inject
	def __init__(
			self,
			file_reader: JsonFileReader,
			logger: CustomLogger):
		"""ConfigValidator __init__."""
		if isinstance(logger, CustomLogger):
			self._logger = logger
			self._logger.log_debug("set: _logger", self._logger)
		else:
			raise TypeError("wrong type for the logger.")

		self._patterns = file_reader.read_(configuration_patterns)
		self._logger.log_debug("set: _patterns", self._patterns)

	def _validate_root_window(self, config: dict) -> bool:
		"""helper for the validate function."""
		keys = {"geometry", "title", "icon", "background"}
		self._logger.log_debug("set: keys", keys)

		if set(config.keys()) != keys:
			self._logger.log_warning(
				"set(config.keys()) != keys", set(config.keys()))
			return False

		for key in config.keys():
			if config[key] is not None:
				if not re.search(self._patterns[key], config[key]):
					self._logger.log_warning(
						"try: re.search(%s, %s)" % (
							self._patterns[key], config[key]))
					return False

			else:
				self._logger.log_warning(
					("try: config['%s'] is None" % key), config[key])
				return False

		self._logger.log_debug(
			"validator admits root_window config", config)
		return True

	def _validate_label(self, config: dict) -> bool:
		"""helper for the validate function."""
		keys = {
			"pos_x",
			"pos_y",
			"width",
			"height",
			"background",
			"foreground",
			"bd",
			"padx",
			"pady",
			"wraplength",
			"anchor",
			"font"}
		self._logger.log_debug("set: keys", keys)

		if set(config.keys()) != keys:
			self._logger.log_warning(
				"set(config.keys()) != keys", set(config.keys()))
			return False

		for key in config.keys():
			if config[key] is not None:
				self._logger.log_debug("value: %s" % key, config[key])

				if self._patterns[key]:
					if not re.search(self._patterns[key], config[key]):
						self._logger.log_warning(
							"try: re.search(%s, %s)" % (
								self._patterns[key], config[key]))
						return False
					else:
						continue

				elif key == "wraplength":
					config[key] = config["width"] - config["padx"] * 2
					self._logger.log_debug(
						("set: config['%s']" % key), config[key])
					continue

				elif key == "anchor":
					if not config[key] in [
						"nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]:
						self._logger.log_warning(
							"try: config['%s'] is not valid key for the anchor" % key,
							config[key])
						return False
					else:
						continue

				elif key in [
					"pos_x", "pos_y", "width", "height", "bd", "padx", "pady"]:
					if not isinstance(config[key], int):
						self._logger.log_warning(
							"try: config['%s'] is not int" % key, config[key])
						return False
					else:
						continue

			else:
				self._logger.log_warning(
					("try: config['%s'] is None" % key), config[key])
				return False

		self._logger.log_debug(
			"validator admits label config", config)
		return True

	def _validate_button(self, config: dict, state: str) -> bool:
		"""helper for the validate function."""
		keys = {
			"pos_x",
			"pos_y",
			"width",
			"height",
			"background",
			"foreground",
			"bd",
			"activebackground",
			"disabledforeground",
			"text"}
		self._logger.log_debug("set: keys", keys)

		if set(config.keys()) != keys:
			self._logger.log_warning(
				"set(config.keys()) != keys", set(config.keys()))
			return False

		for key in config.keys():
			if config[key] is not None:
				self._logger.log_debug("value: %s" % key, config[key])

				if self._patterns[key]:
					if not re.search(self._patterns[key], config[key]):
						self._logger.log_warning(
							"try: re.search(%s, %s)" % (
								self._patterns[key], config[key]))
						return False
					else:
						continue

				elif key in [
					"pos_x", "pos_y", "width", "height", "bd", "padx", "pady"]:
					if not isinstance(config[key], int):
						self._logger.log_warning(
							"try: config['%s'] is not int" % key, config[key])
						return False
					else:
						continue

			else:
				self._logger.log_warning(
					("try: config['%s'] is None" % key), config[key])
				return False

		config["state"] = state
		self._logger.log_debug(
			"validator admits button config", config)
		return True

	def _validate_text(self, config: dict) -> bool:
		"""helper for the validate function."""
		keys = {
			"pos_x",
			"pos_y",
			"width",
			"height",
			"background",
			"foreground",
			"insertbackground",
			"bd",
			"padx",
			"pady",
			"font"}
		self._logger.log_debug("set: keys", keys)

		if set(config.keys()) != keys:
			self._logger.log_warning(
				"set(config.keys()) != keys", set(config.keys()))
			return False

		for key in config.keys():
			if config[key] is not None:
				self._logger.log_debug("value: %s" % key, config[key])

				if self._patterns[key]:
					if not re.search(self._patterns[key], config[key]):
						self._logger.log_warning(
							"try: re.search(%s, %s)" % (
								self._patterns[key], config[key]))
						return False
					else:
						continue

				elif key in [
					"pos_x", "pos_y", "width", "height", "bd", "padx", "pady"]:
					if not isinstance(config[key], int):
						self._logger.log_warning(
							"try: config['%s'] is not int" % key, config[key])
						return False
					else:
						continue

			else:
				self._logger.log_warning(
					("try: config['%s'] is None" % key), config[key])
				return False

		self._logger.log_debug(
			"validator admits text field config", config)
		return True

	def validate(self, config: dict, key: str, state: str = "") -> bool:
		"""validates config."""
		if not isinstance(config, dict) and not isinstance(key, str):
			self._logger.log_warning("try: config", config)
			return False

		if key == "root":
			return self._validate_root_window(config)
		elif key == "label":
			return self._validate_label(config)
		elif key == "button":
			return self._validate_button(config, state)
		elif key == "text":
			return self._validate_text(config)
