"""
contains file path validators.
"""
import re
from abc import abstractmethod, ABC
from dataclasses import dataclass

from injector import singleton


@singleton
@dataclass
class BasePathValidator(ABC):
	"""
	abstract class for path validation.
	"""

	@staticmethod
	@abstractmethod
	def validate_path(*args, **kwargs) -> bool:
		"""
		validates the path.
		:return: boolean.
		"""
		raise NotImplementedError


class PathValidator(BasePathValidator):
	"""
	validator for JSON file paths.
	"""

	@staticmethod
	def validate_path(path: str, pattern: str) -> bool:
		"""
		checks if the path ends with ".json".
		:param path: path to the file.
		:param pattern: file path validation pattern.
		:return: boolean.
		"""
		if isinstance(path, str) and isinstance(pattern, str):
			return bool(re.search(pattern, path))

		else:
			return False
