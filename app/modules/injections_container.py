"""contains injection containers."""
from injector import Binder

from app.modules.base_structures import BaseInjectionContainer


class MainInjectionContainer(BaseInjectionContainer):
	"""main injection container."""

	def configure(self, binder: Binder) -> None:
		"""contains injections and the rules by which injections are
		introduced."""
		...
