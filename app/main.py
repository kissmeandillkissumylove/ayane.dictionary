"""
implementation of a smart dictionary for learning foreign words.
2024/03/31 https://github.com/kissmeandillkissumylove/ayane.dictionary
"""
import tkinter
from abc import ABC, abstractmethod
from typing import Union

from injector import singleton, inject, Injector

from app.config import CONFIG_0, OBJECTS_PLACES
from app.modules.buttons import (
	NextButton, ShowButton, RightButton, WrongButton, AgainButton,
	SaveButton, AddButton, FindButton, EditButton)
from app.modules.config_validator import ConfigValidator
from app.modules.custom_exceptions import ConfigNotFoundError
from app.modules.file_readers import JsonFileReader
from app.modules.labels import (
	ScreenWordLabel, ScreenTranslationLabel, MistakesCounterLabel,
	MistakesTextLabel, WordsTextLabel, WordsCounterLabel,
	WordTextLabel, TranscriptionTextLabel, TranslationTextLabel,
	ResultTextLabel)


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
			injector__: Injector,
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

		self._injector = injector__
		self._config_validator = config_validator
		self._file_reader = file_reader

		self._objects_places = file_reader.read_(OBJECTS_PLACES)

		self._screen_word_label = self._injector.get(ScreenWordLabel)
		self._screen_translation_label = self._injector.get(
			ScreenTranslationLabel)

		self._next_button = self._injector.get(NextButton)
		self._show_button = self._injector.get(ShowButton)
		self._right_button = self._injector.get(RightButton)
		self._wrong_button = self._injector.get(WrongButton)
		self._again_button = self._injector.get(AgainButton)
		self._save_button = self._injector.get(SaveButton)

		self._mistakes_text_label = self._injector.get(MistakesTextLabel)
		self._mistakes_counter_label = self._injector.get(
			MistakesCounterLabel)

		self._add_button = self._injector.get(AddButton)
		self._find_button = self._injector.get(FindButton)
		self._edit_button = self._injector.get(EditButton)

		self._words_text_label = self._injector.get(WordsTextLabel)
		self._words_counter_label = self._injector.get(WordsCounterLabel)

		self._word_text_label = self._injector.get(WordTextLabel)
		self._transcription_text_label = self._injector.get(
			TranscriptionTextLabel)
		self._translation_text_label = self._injector.get(
			TranslationTextLabel)
		self._result_text_label = self._injector.get(ResultTextLabel)

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
		self.resizable(False, False)
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

	@property
	def screen_word_label(self) -> Union[None, ScreenWordLabel]:
		"""
		returns screen_word_label or None.
		:return: label or None.
		"""
		return self._screen_word_label

	@screen_word_label.setter
	def screen_word_label(self, screen_word_label: ScreenWordLabel):
		"""
		sets new value for the _screen_word_label.
		:param screen_word_label: ScreenWordLabel object.
		"""
		if isinstance(screen_word_label, ScreenWordLabel):
			self._screen_word_label = screen_word_label
		else:
			raise ValueError("screen_word_label setter.")

	@property
	def screen_translation_label(
			self) -> Union[None, ScreenTranslationLabel]:
		"""
		returns screen_translation_label or None.
		:return: label or None.
		"""
		return self._screen_translation_label

	@screen_translation_label.setter
	def screen_translation_label(
			self, screen_translation_label: ScreenTranslationLabel):
		"""
		sets new value for the _screen_translation_label.
		:param screen_translation_label: ScreenWordLabel object.
		"""
		if isinstance(screen_translation_label, ScreenTranslationLabel):
			self._screen_translation_label = screen_translation_label
		else:
			raise ValueError("screen_translation_label setter.")

	def setup_all_the_objects_and_run(self):
		"""
		displays all the objects on the screen.
		:return: NoReturn
		"""
		pos = self._objects_places["screen_word_label"].values()
		self._screen_word_label.set_position(*pos)
		pos = self._objects_places["screen_translation_label"].values()
		self._screen_translation_label.set_position(*pos)

		pos = self._objects_places["next_button"].values()
		self._next_button.set_position(*pos)
		pos = self._objects_places["show_button"].values()
		self._show_button.set_position(*pos)
		pos = self._objects_places["right_button"].values()
		self._right_button.set_position(*pos)
		pos = self._objects_places["wrong_button"].values()
		self._wrong_button.set_position(*pos)
		pos = self._objects_places["again_button"].values()
		self._again_button.set_position(*pos)
		pos = self._objects_places["save_button"].values()
		self._save_button.set_position(*pos)

		pos = self._objects_places["mistakes_text_label"].values()
		self._mistakes_text_label.set_position(*pos)
		pos = self._objects_places["mistakes_counter_label"].values()
		self._mistakes_counter_label.set_position(*pos)

		pos = self._objects_places["add_button"].values()
		self._add_button.set_position(*pos)
		pos = self._objects_places["find_button"].values()
		self._find_button.set_position(*pos)
		pos = self._objects_places["edit_button"].values()
		self._edit_button.set_position(*pos)

		pos = self._objects_places["words_text_label"].values()
		self._words_text_label.set_position(*pos)
		pos = self._objects_places["words_counter_label"].values()
		self._words_counter_label.set_position(*pos)

		pos = self._objects_places["word_text_label"].values()
		self._word_text_label.set_position(*pos)
		pos = self._objects_places["transcription_text_label"].values()
		self._transcription_text_label.set_position(*pos)
		pos = self._objects_places["translation_text_label"].values()
		self._translation_text_label.set_position(*pos)
		pos = self._objects_places["result_text_label"].values()
		self._result_text_label.set_position(*pos)

		self.mainloop()


def main():
	"""
	runs application.
	"""
	from app.modules.injector_ import ModuleDI
	_injector_ = Injector([ModuleDI])

	main_window = _injector_.get(MainWindow)
	main_window.setup_all_the_objects_and_run()


if __name__ == "__main__":
	main()
