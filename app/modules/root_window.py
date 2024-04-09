"""contains the main application window."""
from injector import singleton, Injector

from app.modules.base_structures import BaseWindow
from app.modules.logger import CustomLogger


@singleton
class RootWindow(BaseWindow):
	"""main application window."""

	def __init__(self):
		"""RootWindow __init__."""
		super().__init__()

		self._injection_container = None
		self._configuration_dict = None
		self._logger = None

	def _setup_configuration(self, *args, **kwargs):
		"""sets root window configuration."""
		self._logger.log_debug("start _setup_configuration()")

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
			self._logger.log_debug(
				"set: _injection_container",
				self._injection_container)
		else:
			self._logger.log_warning("try: _injection_container", injector)

	@injection_container.deleter
	def injection_container(self):
		"""removes the reference to _injector_container. subsequently this
		object will be deleted."""
		self._logger.log_debug(
			"del: _injection_container",
			self._injection_container)
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
			self._logger.log_debug(
				"set: _configuration_dict",
				self._configuration_dict)
		else:
			self._logger.log_warning("try: _configuration_dict", config)

	@configuration_dict.deleter
	def configuration_dict(self):
		"""removes the reference to _configuration_dict. subsequently this
		object will be deleted."""
		self._logger.log_debug(
			"del: _configuration_dict",
			self._configuration_dict)
		del self._configuration_dict

	@property
	def logger(self) -> CustomLogger:
		"""get _logger value.
		:return: CustomLogger object."""
		return self._logger

	@logger.setter
	def logger(self, new_logger: CustomLogger):
		"""sets new value for _logger.
		:param new_logger: CustomLogger object."""
		if isinstance(new_logger, CustomLogger):
			self._logger = new_logger
			self._logger.log_debug("set: _logger", self._logger)
		else:
			if self._logger is not None:
				self._logger.log_warning("try: _logger", new_logger)

	@logger.deleter
	def logger(self):
		"""removes the reference to _logger. subsequently this
		object will be deleted."""
		self._logger.log_debug("del: _logger", self._logger)
		del self._logger

	def run(self):
		"""launches a window."""
		self._setup_configuration()

		self._logger.log_debug("start main loop. root_window.run()")
		self.mainloop()
