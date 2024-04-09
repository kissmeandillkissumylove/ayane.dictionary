"""contains injection containers."""
from injector import Binder

from app.modules.base_structures import BaseInjectionContainer
from app.modules.logger import CustomLogger


class MainInjectionContainer(BaseInjectionContainer):
	"""main injection container."""

	def configure(self, binder: Binder) -> None:
		"""contains injections and the rules by which injections are
		introduced."""
		binder.bind(CustomLogger, to=CustomLogger(__name__, 10))
