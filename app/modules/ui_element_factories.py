"""contains user interface element factories."""
import tkinter
from tkinter import WORD

from injector import inject

from app.modules.button_commands import CommandsContainer
from app.modules.logger import CustomLogger


class CreateLabel(tkinter.Label):
	"""creates a label object and can place it on the screen."""

	@inject
	def __init__(self, logger: CustomLogger):
		"""CreateLabel __init__."""
		super().__init__()

		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong type for the logger.")

		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

	def set_configuration(self, config: dict):
		"""sets configuration for the label"""
		if not isinstance(config, dict):
			self._logger.log_error("try: config", config)
			return

		self._logger.log_debug("run: set_configuration()", config)
		self._logger.log_debug(
			"value: config['wraplength']", config["wraplength"])

		self.configure(
			background=config["background"],
			foreground=config["foreground"],
			bd=config["bd"],
			padx=config["padx"],
			pady=config["pady"],
			wraplength=config["wraplength"],
			anchor=config["anchor"],
			font=config["font"])

		self._set_place(config)

	def _set_place(self, config: dict):
		"""sets label position."""
		self._logger.log_debug("run: _set_place")

		if not isinstance(config, dict):
			self._logger.log_critical("try: config", config)
			raise TypeError("wrong type for the config.")

		self.place(
			x=config["pos_x"], y=config["pos_y"],
			width=config["width"], height=config["height"])


class CreateButton(tkinter.Button):
	"""creates a button object and can place it on the screen."""

	@inject
	def __init__(self, logger: CustomLogger):
		"""CreateButton __init__."""
		super().__init__()

		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong type for the logger.")

		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

	def set_configuration(self, config: dict, command: str):
		"""sets configuration for the label"""
		if not isinstance(config, dict):
			self._logger.log_error("try: config", config)
			return

		if not isinstance(command, str):
			self._logger.log_error("try: command", command)
			return

		self._logger.log_debug("run: set_configuration()", config)

		self.configure(
			background=config["background"],
			foreground=config["foreground"],
			bd=config["bd"],
			activebackground=config["activebackground"],
			disabledforeground=config["disabledforeground"],
			text=config["text"],
			state=config["state"],
			command=getattr(CommandsContainer, command)
		)

		self._set_place(config)

	def _set_place(self, config: dict):
		"""sets label position."""
		self._logger.log_debug("run: _set_place")

		if not isinstance(config, dict):
			self._logger.log_critical("try: config", config)
			raise TypeError("wrong type for the config.")

		self.place(
			x=config["pos_x"], y=config["pos_y"],
			width=config["width"], height=config["height"])


class CreateText(tkinter.Text):
	"""creates a text field object and can place it on the screen."""

	@inject
	def __init__(self, logger: CustomLogger):
		"""CreateLabel __init__."""
		super().__init__()

		if not isinstance(logger, CustomLogger):
			raise TypeError("wrong type for the logger.")

		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

	def set_configuration(self, config: dict):
		"""sets configuration for the text field"""
		if not isinstance(config, dict):
			self._logger.log_error("try: config", config)
			return

		self._logger.log_debug("run: set_configuration()", config)

		self.configure(
			background=config["background"],
			foreground=config["foreground"],
			insertbackground=config["insertbackground"],
			bd=config["bd"],
			padx=config["padx"],
			pady=config["pady"],
			font=config["font"],
			wrap=WORD)

		self._set_place(config)

	def _set_place(self, config: dict):
		"""sets text field position."""
		self._logger.log_debug("run: _set_place")

		if not isinstance(config, dict):
			self._logger.log_critical("try: config", config)
			raise TypeError("wrong type for the config.")

		self.place(
			x=config["pos_x"], y=config["pos_y"],
			width=config["width"], height=config["height"])
