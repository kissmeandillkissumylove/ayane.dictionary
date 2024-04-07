"""contains the main application window."""
from injector import singleton, Injector

from app.modules.base_structures import BaseWindow


@singleton
class RootWindow(BaseWindow):
	"""main application window."""

	def __init__(self):
		"""RootWindow __init__."""
		super().__init__()

		self._injection_container = None
		self._configuration_dict = None

	def _setup_configuration(self, *args, **kwargs):
		"""sets root window configuration."""
		pass

	@property
	def injection_container(self) -> Injector:
		"""get _injection_container value.
		:return: Injector objects."""
		return self._injection_container

	@injection_container.setter
	def injection_container(self, injector: Injector):
		"""sets new value for _injector_container.
		:param injector: Injector object."""
		if isinstance(injector, Injector):
			self._injection_container = injector
		else:
			pass

	@injection_container.deleter
	def injection_container(self):
		"""removes the reference to _injector_container. subsequently this
		object will be deleted."""
		del self._injection_container

	@property
	def configuration_dict(self) -> dict:
		"""get _configuration_dict value.
		:return: dict object."""
		return self._configuration_dict

	@configuration_dict.setter
	def configuration_dict(self, config: dict):
		"""sets new value for _configuration_dict.
		:param config: dict object."""
		if isinstance(config, dict):
			self._configuration_dict = config
		else:
			pass

	@configuration_dict.deleter
	def configuration_dict(self):
		"""removes the reference to _configuration_dict. subsequently this
		object will be deleted."""
		del self._configuration_dict

	def run(self):
		"""launches a window."""
		self._setup_configuration()
		self.mainloop()
