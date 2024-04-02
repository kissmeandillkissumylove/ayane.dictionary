"""
contains a container with injections that are needed for dependencies in the
code.
"""
from injector import Module, Binder, singleton

from app.modules.file_readers import JsonFileReader
from app.modules.path_validators import BasePathValidator, JsonPathValidator


@singleton
class ModuleDI(Module):
	"""
	main container with injections.
	"""

	def configure(self, binder: Binder) -> None:
		"""
		creates instances of objects and injects dependencies wherever the
		@inject decorator requires them.
		:param binder: (injector.Binder) an object used to register dependencies
			and configure the injector.
		:return: None.
		"""
		binder.bind(BasePathValidator, to=JsonPathValidator)
		binder.bind(JsonPathValidator)
		binder.bind(JsonFileReader)