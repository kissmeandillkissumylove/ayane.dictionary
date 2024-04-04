"""
implementation of a smart dictionary for learning foreign words.
2024/03/31 https://github.com/kissmeandillkissumylove/ayane.dictionary
"""
import tkinter
from abc import ABC, abstractmethod
from typing import Union

from injector import singleton, inject, Injector

from app.config import CONFIG_0
from app.modules.config_validator import ConfigValidator
from app.modules.custom_exceptions import ConfigNotFoundError
from app.modules.file_readers import JsonFileReader


@singleton
class BaseWindow(ABC, tkinter.Tk):
	"""
	abstract class for tkinter window.
	"""

	@abstractmethod
	def __init__(self):
		super().__init__()

	@abstractmethod
	def _setup_config(self, *args, **kwargs):
		raise NotImplementedError


class MainWindow(BaseWindow):
	"""
	main application class. creates the main window.
	"""

	@inject
	def __init__(
			self,
			config_validator: ConfigValidator,
			file_reader: JsonFileReader,
			config: dict = None):
		"""
		initializes the application main window.
		:param config: a dictionary containing configuration options for the
			application window. defaults to None. valid keys include:
				- geometry (str): the window geometry. the window size is
					currently limited, but you can specify a shift by coordinates
					(e.g. "500x265+500+200", "500x265+100", "500x265").
				- title (str): the title of the application window. (not more than
					32 symbols.)
				- icon (str or pathlib.Path): path to the application icon.
				- background (str): background color (e.g., "#ffffff", "#2D81B2").
				"""
		super().__init__()

		self._injector = None
		self._config_validator = config_validator
		self._file_reader = file_reader

		if config and self._config_validator.validate(config):
			self._setup_config(config)

		else:
			config = file_reader.read_(CONFIG_0)
			if config and config_validator.validate(config):
				self._setup_config(config)

			else:
				raise ConfigNotFoundError(f"file '{CONFIG_0}' not found.")

	def _setup_config(self, config: dict):
		"""
		set settings by configuration dictionary.
		:param config: dictionary with values.
		:return: NoReturn.
		"""
		self.geometry(config["geometry"])
		self.title(config["title"])

		try:
			self.iconbitmap(config["icon"])
		except tkinter.TclError:
			pass

		self.configure(background=config["background"])

	@property
	def injector(self) -> Injector:
		"""
		:return: injector.
		"""
		return self._injector

	@injector.setter
	def injector(self, new_injector: Injector):
		"""
		sets new injector.
		:return: NoReturn.
		"""
		if isinstance(new_injector, Injector):
			self._injector = new_injector


def main():
	"""
	runs application.
	"""
	from app.modules.injector_ import ModuleDI
	_injector_ = Injector([ModuleDI])

	main_window = _injector_.get(MainWindow)
	main_window.injector = _injector_

	main_window.mainloop()


if __name__ == "__main__":
	main()
