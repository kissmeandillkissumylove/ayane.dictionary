"""an application logger is here."""
import logging

from injector import singleton

from app.config import logs
from app.modules.base_structures import BaseLogger


@singleton
class CustomLogger(BaseLogger):
	"""application logger."""

	def __init__(self, name: str, level: int = 30):
		"""CustomLogger __init__."""
		if isinstance(name, str):
			super().__init__(name)

			self._logger = logging.getLogger()
			self.set_logger_level(level)
			self._setup_logger(name)

		else:
			raise TypeError("%s is not str." % name)

	def _setup_logger(self, name: str):
		"""sets settings for the logger."""
		formatter_debug = logging.Formatter(
			fmt=
			"%(levelname)-12s"
			"%(asctime)-30s"
			"%(filename)-25s"
			"%(lineno)-12s"
			"%(message)-s",
			datefmt="%Y-%m-%d %H:%M:%S")

		handler_debug = logging.FileHandler(
			filename=logs,
			mode="a",
			encoding="utf-8")

		handler_debug.setLevel(logging.DEBUG)

		handler_debug.setFormatter(formatter_debug)

		self._logger.addHandler(handler_debug)

	def set_logger_level(self, level: int):
		"""sets logging level."""
		if level == 10:
			self._logger.setLevel(logging.DEBUG)

		elif level == 20:
			self._logger.setLevel(logging.INFO)

		elif level == 30:
			self._logger.setLevel(logging.WARNING)

		elif level == 40:
			self._logger.setLevel(logging.ERROR)

		elif level == 50:
			self._logger.setLevel(logging.CRITICAL)

		else:
			raise ValueError("wrong value for the logger.")

	def log(self, level: int, message: str, *args, **kwargs):
		"""write the message to the log file."""
		if level == 10:
			self._logger.debug(message)

		elif level == 20:
			self._logger.info(message)

		elif level == 30:
			self._logger.warning(message)

		elif level == 40:
			self._logger.error(message)

		elif level == 50:
			self._logger.critical(message)

		else:
			raise ValueError("wrong value for the logger.")
