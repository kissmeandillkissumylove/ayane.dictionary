"""contains the main application window."""
from injector import singleton, inject, Injector

from app.modules.base_structures import BaseWindow
from app.modules.containers import ConfigContainer
from app.modules.logger import CustomLogger
from app.modules.ui_element_factories import CreateLabel, CreateButton


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

			self._screen_word_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _screen_word_label", self._screen_word_label)
			self._screen_word_label.set_configuration(
				self._configuration_container.screen_word_label)

			self._screen_translation_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _screen_translation_label",
				self._screen_translation_label)
			self._screen_translation_label.set_configuration(
				self._configuration_container.screen_translation_label)

			self._next_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _next_button", self._next_button)
			self._next_button.set_configuration(
				self._configuration_container.next_button,
				"next_command")

			self._show_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _show_button", self._show_button)
			self._show_button.set_configuration(
				self._configuration_container.show_button,
				"show_command")

			self._right_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _right_button", self._right_button)
			self._right_button.set_configuration(
				self._configuration_container.right_button,
				"right_command")

			self._wrong_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _wrong_button", self._wrong_button)
			self._wrong_button.set_configuration(
				self._configuration_container.wrong_button,
				"wrong_command")

			self._again_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _again_button", self._again_button)
			self._again_button.set_configuration(
				self._configuration_container.again_button,
				"again_command")

			self._save_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _save_button", self._save_button)
			self._save_button.set_configuration(
				self._configuration_container.save_button,
				"save_command")

			self._add_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _add_button", self._add_button)
			self._add_button.set_configuration(
				self._configuration_container.add_button,
				"add_command")

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

	@property
	def injection_container(self) -> Injector:
		"""get _injection_container value.
		:return: Injector object."""
		return self._injection_container

	@injection_container.setter
	def injection_container(self, new_injector: Injector):
		"""sets new value for _injection_container.
		:param new_injector: Injector object."""
		if not isinstance(new_injector, Injector):
			self._logger.log_warning("try: _injection_container")
		else:
			self._injection_container = new_injector
			self._logger.log_debug(
				"set: _injection_container", self._injection_container)

	@injection_container.deleter
	def injection_container(self):
		"""removes the reference to _injection_container.
		subsequently this object will be deleted."""
		self._logger.log_debug(
			"del: _injection_container",
			self._injection_container)
		del self._injection_container

	def run(self):
		"""launches a window."""
		self._setup_configuration()

		self._logger.log_debug("start self.mainloop()")
		self.mainloop()
