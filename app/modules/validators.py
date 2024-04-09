"""contains file path validators."""
import re

from app.modules.base_structures import BaseValidator
from app.modules.logger import CustomLogger


class PathValidator(BaseValidator):
	"""validator for file paths."""

	@staticmethod
	def validate(
			logger: CustomLogger,
			path: str,
			pattern: str) -> bool:
		"""checks if the path ends with "*.extension".
		:param logger: CustomLogger object.
		:param path: path to the file.
		:param pattern: file path validation pattern.
		:return: boolean.
		"""
		logger.log_debug("value: path", path)
		logger.log_debug("value: pattern", pattern)

		if isinstance(path, str) and isinstance(pattern, str):
			return bool(re.search(pattern, path))
		else:
			return False
