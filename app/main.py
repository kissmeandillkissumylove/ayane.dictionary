import tkinter

from modules.JSONReader import JSONReader
from modules.config_validator import ConfigValidator
from modules.paths import CONFIG_0


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
