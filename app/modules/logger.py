"""application logger."""
import inspect
import logging
import re
from logging.handlers import RotatingFileHandler
from typing import Tuple, Any

from injector import singleton

from app.config import (
	MAX_VALUE_LENGTH, logs, LOG_SIZE_LIMIT, NUM_LOG_FILES)
from app.modules.base_structures import BaseLogger


@singleton
class CustomLogger(BaseLogger):
	"""logger."""

	def __init__(self, name: str, level: int):
		"""Logger __init__."""
		super().__init__(name)

		self._file = logs
		self._pattern = "\\.log$"
		self._logger = None

		self._setup_logger(level)

	@property
	def file(self) -> str:
		"""returns path to the log file."""
		return self._file

	@file.setter
	def file(self, path: str):
		"""sets new path to the log file."""
		if bool(re.search(self._pattern, path)):
			self._file = path
		else:
			raise ValueError("wrong value for the path.")

	@file.deleter
	def file(self):
		"""removes the reference to _file. subsequently this
		object will be deleted."""
		del self._file

	def _setup_logger(self, level: int):
		"""sets settings for the logger."""
		if level not in [10, 20, 30, 40, 50]:
			raise ValueError("level value error.")

		self._logger = logging.getLogger()
		self._logger.setLevel(level)

		formatter_ = logging.Formatter(
			fmt="%(levelname)-10s%(asctime)-21s%(message)-s",
			datefmt="%Y-%m-%d %H:%M:%S")

		handler_ = RotatingFileHandler(
			filename=self._file,
			maxBytes=LOG_SIZE_LIMIT,
			backupCount=NUM_LOG_FILES,
			mode="a",
			encoding="utf-8")

		handler_.setLevel(logging.DEBUG)
		handler_.setFormatter(formatter_)

		self._logger.addHandler(handler_)

	@staticmethod
	def _get_caller_info() -> Tuple[str, int]:
		"""returns module caller name and code line."""
		frame = inspect.currentframe().f_back.f_back.f_back

		module_name, lineno = "unknown", 0
		if frame is not None:
			module = inspect.getmodule(frame)

			if module is not None:
				module_name = module.__name__

			lineno = frame.f_lineno

		return module_name, lineno

	@staticmethod
	def _truncate_value(value: str) -> Any:
		"""returns value trimmed to MAX_VALUE_LENGTH."""
		if len(value) > MAX_VALUE_LENGTH:
			value = value[:MAX_VALUE_LENGTH - 3] + "..."

		return value

	def _log_message(
			self, level: str,
			message: str,
			arg: Any = None,
			edit: str = "yes"):
		"""prepares and writes logger message."""
		if level not in ["debug", "info", "warning", "error", "critical"]:
			raise ValueError("level value error.")

		if not isinstance(message, str):
			raise TypeError("wrong type for the message")

		module_name, lineno = self._get_caller_info()

		if edit == "no":
			formatted_message = "%-25s%-8s%-s" % (
				module_name, lineno, message)
			getattr(self._logger, level)(formatted_message)
			return

		message = self._truncate_value(message)

		formatted_message = "%-25s%-8s%-52s" % (
			module_name, lineno, message)

		if arg is not None:
			truncated_value = self._truncate_value(str(arg))
			formatted_message += "%-20s%-30s%-52s" % (
				id(arg), type(arg).__name__, truncated_value)

		getattr(self._logger, level)(formatted_message)

	def log_debug(self, message: str, arg: Any = None):
		"""write a message with "debug" level."""
		self._log_message("debug", message, arg)

	def log_info(self, message: str, arg: Any = None):
		"""write a message with "info" level."""
		self._log_message("info", message, arg)

	def log_warning(self, message: str, arg: Any = None):
		"""write a message with "warning" level."""
		self._log_message("warning", message, arg)

	def log_error(self, message: str, arg: Any = None):
		"""write a message with "error" level."""
		self._log_message("error", message, arg)

	def log_critical(self, message: str, arg: Any = None):
		"""write a message with "critical" level."""
		self._log_message("critical", message, arg)

	def log_escape(self, message: str, edit: str = "no"):
		"""write a message with "critical" level."""
		self._log_message("critical", message=message, edit=edit)
