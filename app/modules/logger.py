"""an application logger is here."""
import logging
from logging.handlers import RotatingFileHandler

from injector import singleton, inject

from app.config import logs, LOG_SIZE_LIMIT, NUM_LOG_FILES
from app.modules.base_structures import BaseLogger


@singleton
class CustomLogger(BaseLogger):
	"""application logger."""

	@inject
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
		formatter_ = logging.Formatter(
			fmt=
			"%(levelname)-12s"
			"%(asctime)-30s"
			"%(filename)-25s"
			"%(lineno)-12s"
			"%(message)-s",
			datefmt="%Y-%m-%d %H:%M:%S")

		handler_ = RotatingFileHandler(
			filename=logs,
			maxBytes=LOG_SIZE_LIMIT,
			backupCount=NUM_LOG_FILES,
			mode="a",
			encoding="utf-8")

		handler_.setLevel(logging.DEBUG)
		handler_.setFormatter(formatter_)
		self._logger.addHandler(handler_)

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
