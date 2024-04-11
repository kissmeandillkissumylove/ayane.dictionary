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
		self._configuration = None
		self._logger = None

	def _setup_configuration(self, *args, **kwargs):
		"""sets root window configuration."""
		if self._configuration is not None:
			self._logger.log_debug("start _setup_configuration()")

			self.geometry(self._configuration["geometry"])
			self._logger.log_debug(
				"set: geometry", self._configuration["geometry"])

			self.resizable(False, False)
			self._logger.log_debug("set: resizable(False, False)")

			self.title(self._configuration["title"])
			self._logger.log_debug("set: title", self._configuration["title"])

			self.iconbitmap(self._configuration["icon"])
			self._logger.log_debug(
				"set: iconbitmap", self._configuration["icon"])

			self.configure(background=self._configuration["background"])
			self._logger.log_debug(
				"set: background", self._configuration["background"])

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
	def configuration(self) -> dict:
		"""get _configuration value.
		:return: dict object."""
		return self._configuration

	@configuration.setter
	def configuration(self, config: dict):
		"""sets new value for _configuration.
		:param config: dict object."""
		if isinstance(config, dict):
			self._configuration = config
			self._logger.log_debug(
				"set: _configuration",
				self._configuration)
		else:
			self._logger.log_warning("try: _configuration", config)

	@configuration.deleter
	def configuration(self):
		"""removes the reference to _configuration. subsequently this
		object will be deleted."""
		self._logger.log_debug(
			"del: _configuration",
			self._configuration)
		del self._configuration

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

		self._logger.log_debug("start self.mainloop()")
		self.mainloop()
