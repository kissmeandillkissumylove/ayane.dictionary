"""contains the main application window."""
from injector import singleton, inject, Injector

from app.modules.base_structures import BaseWindow
from app.modules.containers import (
	ConfigContainer, DictionaryContainer)
from app.modules.logger import CustomLogger
from app.modules.ui_element_factories import (
	CreateLabel, CreateButton, CreateText)


@singleton
class RootWindow(BaseWindow):
	"""main application window."""

	@inject
	def __init__(
			self,
			logger: CustomLogger,
			dictionary: DictionaryContainer):
		"""RootWindow __init__."""
		super().__init__()

		if not isinstance(logger, CustomLogger):
			raise TypeError(
				"wrong type for the logger. %s" % type(logger))
		self._logger = logger
		self._logger.log_debug("set: _logger", self._logger)

		if not isinstance(dictionary, DictionaryContainer):
			raise TypeError(
				"wrong type for the dictionary. %s" % type(dictionary))
		self._dictionary = dictionary
		self._logger.log_debug("set: _dictionary", self._dictionary)

		self._configuration_container = None
		self._injection_container = None
		self._counter = 0

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
				"next_command", self)

			self._show_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _show_button", self._show_button)
			self._show_button.set_configuration(
				self._configuration_container.show_button,
				"show_command", self)

			self._right_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _right_button", self._right_button)
			self._right_button.set_configuration(
				self._configuration_container.right_button,
				"right_command", self)

			self._wrong_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _wrong_button", self._wrong_button)
			self._wrong_button.set_configuration(
				self._configuration_container.wrong_button,
				"wrong_command", self)

			self._again_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _again_button", self._again_button)
			self._again_button.set_configuration(
				self._configuration_container.again_button,
				"again_command", self)

			self._add_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _add_button", self._add_button)
			self._add_button.set_configuration(
				self._configuration_container.add_button,
				"add_command", self)

			self._find_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _find_button", self._find_button)
			self._find_button.set_configuration(
				self._configuration_container.find_button,
				"find_command", self)

			self._edit_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _edit_button", self._edit_button)
			self._edit_button.set_configuration(
				self._configuration_container.edit_button,
				"edit_command", self)

			self._remove_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _remove_button", self._remove_button)
			self._remove_button.set_configuration(
				self._configuration_container.remove_button,
				"remove_command", self)

			self._save_button = self.injection_container.get(
				CreateButton)
			self._logger.log_debug(
				"set: _save_button", self._save_button)
			self._save_button.set_configuration(
				self._configuration_container.save_button,
				"save_command", self)

			self._words_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _words_label", self._words_label)
			self._words_label.set_configuration(
				self._configuration_container.words_label)
			self._words_label.configure(text="ᴡᴏʀᴅs:")

			self._words_counter_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _words_counter_label", self._words_counter_label)
			self._words_counter_label.set_configuration(
				self._configuration_container.words_counter_label)
			self._words_counter_label.configure(
				text="%s/%s" % (
					self._counter, len(self._dictionary.sorted_dictionary)))

			self._mistakes_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _mistakes_label", self._mistakes_label)
			self._mistakes_label.set_configuration(
				self._configuration_container.mistakes_label)
			self._mistakes_label.configure(text="ᴍɪsᴛᴀᴋᴇs:")

			self._mistakes_counter_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _mistakes_counter_label",
				self._mistakes_counter_label)
			self._mistakes_counter_label.set_configuration(
				self._configuration_container.mistakes_counter_label)
			self._mistakes_counter_label.configure(text=0)

			self._word_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _word_label", self._word_label)
			self._word_label.set_configuration(
				self._configuration_container.word_label)
			self._word_label.configure(text="ᴡᴏʀᴅ:")

			self._word_text = self.injection_container.get(
				CreateText)
			self._logger.log_debug(
				"set: _word_text", self._word_text)
			self._word_text.set_configuration(
				self._configuration_container.word_text)

			self._transcription_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _transcription_label", self._transcription_label)
			self._transcription_label.set_configuration(
				self._configuration_container.transcription_label)
			self._transcription_label.configure(text="ᴛʀᴀɴsᴄʀɪᴘᴛɪᴏɴ:")

			self._transcription_text = self.injection_container.get(
				CreateText)
			self._logger.log_debug(
				"set: _transcription_text", self._transcription_text)
			self._transcription_text.set_configuration(
				self._configuration_container.transcription_text)

			self._part_of_speech_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _part_of_speech_label",
				self._part_of_speech_label)
			self._part_of_speech_label.set_configuration(
				self._configuration_container.part_of_speech_label)
			self._part_of_speech_label.configure(text="ᴘᴀʀᴛ ᴏꜰ sᴘᴇᴇᴄʜ:")

			self._part_of_speech_text = self.injection_container.get(
				CreateText)
			self._logger.log_debug(
				"set: _part_of_speech_text", self._part_of_speech_text)
			self._part_of_speech_text.set_configuration(
				self._configuration_container.part_of_speech_text)

			self._usage_example_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _usage_example_label",
				self._usage_example_label)
			self._usage_example_label.set_configuration(
				self._configuration_container.usage_example_label)
			self._usage_example_label.configure(text="ᴜsᴀɢᴇ ᴇxᴀᴍᴘʟᴇ:")

			self._usage_example_text = self.injection_container.get(
				CreateText)
			self._logger.log_debug(
				"set: _usage_example_text", self._usage_example_text)
			self._usage_example_text.set_configuration(
				self._configuration_container.usage_example_text)

			self._translation_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _translation_label", self._translation_label)
			self._translation_label.set_configuration(
				self._configuration_container.translation_label)
			self._translation_label.configure(text="ᴛʀᴀɴsʟᴀᴛɪᴏɴ:")

			self._translation_text = self.injection_container.get(
				CreateText)
			self._logger.log_debug(
				"set: _translation_text", self._translation_text)
			self._translation_text.set_configuration(
				self._configuration_container.translation_text)

			self._result_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _result_label", self._result_label)
			self._result_label.set_configuration(
				self._configuration_container.result_label)
			self._result_label.configure(text="ʀᴇsᴜʟᴛ:")

			self._command_label = self.injection_container.get(
				CreateLabel)
			self._logger.log_debug(
				"set: _command_label", self._command_label)
			self._command_label.set_configuration(
				self._configuration_container.command_label)

	@property
	def configuration_container(self) -> ConfigContainer:
		"""get _configuration_container value.
		:return: ConfigContainer object."""
		return self._configuration_container

	@configuration_container.setter
	def configuration_container(self, container: ConfigContainer):
		"""sets new value for _configuration_container.
		:param container: ConfigContainer object."""
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

	@property
	def screen_word_label(self):
		return self._screen_word_label

	@property
	def screen_translation_label(self):
		return self._screen_translation_label

	@property
	def next_button(self):
		return self._next_button

	@property
	def show_button(self):
		return self._show_button

	@property
	def right_button(self):
		return self._right_button

	@property
	def wrong_button(self):
		return self._wrong_button

	@property
	def again_button(self):
		return self._again_button

	@property
	def add_button(self):
		return self._add_button

	@property
	def find_button(self):
		return self._find_button

	@property
	def edit_button(self):
		return self._edit_button

	@property
	def remove_button(self):
		return self._remove_button

	@property
	def save_button(self):
		return self._save_button

	@property
	def words_label(self):
		return self._words_label

	@property
	def words_counter_label(self):
		return self._words_counter_label

	@property
	def mistakes_label(self):
		return self._mistakes_label

	@property
	def mistakes_counter_label(self):
		return self._mistakes_counter_label

	@property
	def word_label(self):
		return self._word_label

	@property
	def word_text(self):
		return self._word_text

	@property
	def transcription_label(self):
		return self._transcription_label

	@property
	def transcription_text(self):
		return self._transcription_text

	@property
	def part_of_speech_label(self):
		return self._part_of_speech_label

	@property
	def part_of_speech_text(self):
		return self._part_of_speech_text

	@property
	def usage_example_label(self):
		return self._usage_example_label

	@property
	def usage_example_text(self):
		return self._usage_example_text

	@property
	def translation_label(self):
		return self._translation_label

	@property
	def translation_text(self):
		return self._translation_text

	@property
	def result_label(self):
		return self._result_label

	@property
	def command_label(self):
		return self._command_label

	@property
	def dictionary_container(self):
		return self._dictionary

	@property
	def counter(self):
		return self._counter

	@counter.setter
	def counter(self, value: int):
		self._counter = value

	def run(self):
		"""launches a window."""
		self._dictionary.preload_dictionary()

		self._setup_configuration()

		self._logger.log_debug("start self.mainloop()")
		self.mainloop()
