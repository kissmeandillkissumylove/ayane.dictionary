"""contains injection containers."""
from injector import Binder, provider

from app.modules.base_structures import BaseInjectionContainer
from app.modules.logger import CustomLogger


class MainInjectionContainer(BaseInjectionContainer):
	"""main injection container."""

	@provider
	def provide_custom_logger(self) -> CustomLogger:
		"""returns CustomLogger object."""
		return CustomLogger(__name__)

	def configure(self, binder: Binder) -> None:
		"""contains injections and the rules by which injections are
		introduced."""
		binder.bind(CustomLogger, to=self.provide_custom_logger)
