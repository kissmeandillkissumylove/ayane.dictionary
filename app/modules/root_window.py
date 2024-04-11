"""contains the main application window."""
from injector import singleton, inject

from app.modules.base_structures import BaseWindow
from app.modules.logger import CustomLogger


@singleton
class RootWindow(BaseWindow):
	"""main application window."""

	@inject
	def __init__(self, logger: CustomLogger):
		"""RootWindow __init__."""
		super().__init__()

		if isinstance(logger, CustomLogger):
			self._logger = logger
		else:
			raise TypeError("wrong type for the logger. %s" % type(logger))

		self._injection_container = None
		self._configuration = None

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

	def run(self):
		"""launches a window."""
		self._setup_configuration()

		self._logger.log_debug("start self.mainloop()")
		self.mainloop()
