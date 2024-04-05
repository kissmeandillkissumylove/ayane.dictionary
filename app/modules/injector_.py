"""
contains a container with injections that are needed for dependencies in
the code.
"""
from injector import Module, Binder

from app.main import MainWindow
from app.modules.config_validator import (
	JsonTypesContainer, ConfigValidationContainer, ConfigValidator,
	BaseValidator)
from app.modules.file_readers import JsonFileReader
from app.modules.labels import ScreenWordLabel, ScreenTranslationLabel
from app.modules.path_validators import PathValidator


class ModuleDI(Module):
	"""
	main container with injections.
	"""

	def configure(self, binder: Binder) -> None:
		"""
		creates instances of objects and injects dependencies wherever the
		@inject decorator requires them.
		:param binder: (injector.Binder) an object used to register
			dependencies and configure the injector.
		:return: None.
		"""
		binder.bind(JsonFileReader, to=JsonFileReader)
		binder.bind(JsonTypesContainer, to=JsonTypesContainer)
		binder.bind(ConfigValidationContainer, to=ConfigValidationContainer)
		binder.bind(BaseValidator, to=PathValidator)
		binder.bind(ConfigValidator, to=ConfigValidator)

		binder.bind(ScreenWordLabel, to=ScreenWordLabel)
		binder.bind(ScreenTranslationLabel, to=ScreenTranslationLabel)

		binder.bind(MainWindow, to=MainWindow)
