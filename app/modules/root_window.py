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

		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong type for the logger. %s" % type(logger))
		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

		self._configuration_container = None
		self._injection_container = None

	def _setup_configuration(self, *args, **kwargs):
		"""sets root window configuration."""
		if self._configuration_container is not None:
			root_config = self._configuration_container.root_window
			self._logger.log_debug(
				"start _setup_configuration()", root_config)

			self.geometry(root_config["geometry"])
			self._logger.log_debug(
				"set: geometry", root_config["geometry"])

			self.resizable(False, False)
			self._logger.log_debug("set: resizable(False, False)")

			self.title(root_config["title"])
			self._logger.log_debug("set: title", root_config["title"])

			self.iconbitmap(root_config["icon"])
			self._logger.log_debug(
				"set: iconbitmap", root_config["icon"])

			self.configure(background=root_config["background"])
			self._logger.log_debug(
				"set: background", root_config["background"])

	@property
	def configuration_container(self) -> ConfigContainer:
		"""get _configuration_container value.
		:return: ConfigContainer object."""
		return self._configuration_container

	@configuration_container.setter
	def configuration_container(self, container: ConfigContainer):
		"""sets new value for _configuration_container.
		:param config: ConfigContainer object."""
		if isinstance(container, ConfigContainer):
			self._configuration_container = container
			self._logger.log_debug(
				"set: _configuration",
				self._configuration_container)
		else:
			self._logger.log_warning(
				"try: _configuration_container", container)

	@configuration_container.deleter
	def configuration_container(self):
		"""removes the reference to _configuration_container.
		subsequently this object will be deleted."""
		self._logger.log_debug(
			"del: _configuration",
			self._configuration_container)
		del self._configuration_container

	def run(self):
		"""launches a window."""
		self._setup_configuration()

		self._logger.log_debug("start self.mainloop()")
		self.mainloop()
