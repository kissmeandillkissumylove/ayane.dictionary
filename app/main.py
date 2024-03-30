import re
import tkinter

from modules.JSONReader import JSONReader
from modules.config_validation_types import ValidationTypes
from modules.paths import CONFIG_TEMPLATE, CONFIG_0


class ConfigValidationTemplate:
	"""
	contains valid types and patterns for checking the configuration file.
	"""

	def __init__(self):
		"""
		contains valid types and patterns for checking the configuration file.
		"""
		self._template = {
			"types": ValidationTypes.load_types(),
			"patterns": JSONReader.read_json(CONFIG_TEMPLATE)
		}

	def get_types(self) -> dict:
		"""
		:return: types dictionary.
		"""
		return self._template["types"]

	def get_patters(self) -> dict:
		"""
		:return: patterns dictionary.
		"""
		return self._template["patterns"]


class ConfigValidator:
	"""
	checks the validity of the configuration file.
	"""

	@classmethod
	def validate_config(cls, config: dict) -> bool:
		"""
		checks that the config matches the types and template.
		:param config: config dictionary.
		:return: boolean.
		"""
		config_template = ConfigValidationTemplate()
		for key, value in config.items():
			if key not in config_template.get_types():
				return False
			if type(value) not in config_template.get_types()[key]:
				return False
			if not re.search(config_template.get_patters()[key], value):
				return False
		return True


class App(tkinter.Tk):
	"""
	main application class. creates main window.
	"""

	def __init__(self, config: dict = None):
		"""
		initializes the application window.
		:param config: a dictionary containing configuration options for the
			application window. defaults to None. valid keys include:
				- geometry (str): the window geometry (e.g., "800x600+100+200").
				- title (str): the title of the application window.
				- icon (str or pathlib.Path): path to the application icon.
				- background (str): background color (e.g., "#ffffff", "#2D81B2").
		"""
		super().__init__()

		if config and ConfigValidator.validate_config(config):
			self._config_setup(config)

		else:
			config = JSONReader.read_json(CONFIG_0)
			if config and ConfigValidator.validate_config(config):
				self._config_setup(config)

	def _config_setup(self, config: dict):
		"""
		set settings by configuration dictionary.
		:param config: dictionary.
		"""
		self.geometry(config["geometry"])
		self.title(config["title"])
		try:
			self.iconbitmap(config["icon"])
		except tkinter.TclError:
			pass
		self.configure(background=config["background"])


def main():
	"""
	main function. runs application.
	"""
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()
