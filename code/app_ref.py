"""it's an implementation of dictionary on cards by ayane miuro.
02/07/2024 - 03/18/2024 https://github.com/kissmeandillkissumylove"""
from constants import *
from dataclasses import dataclass, field
import tkinter
from tkinter import NW, W, WORD, ttk


class Singleton(object):
	"""singleton implementation."""
	_instance = None

	def __new__(cls, *args, **kwargs):
		"""method __new__ of class Singleton."""
		if not isinstance(cls._instance, cls):
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def __del__(self):
		"""method __del__ of class Singleton."""
		Singleton._instance = None


@dataclass
class Dictionary(Singleton):
	"""a dataclass used to store all the words."""
	_dictionary: dict = field(default_factory=dict)
	_len: int = 0

	def _preload_dictionary(self, path=DATABASE_PATH) -> None:
		"""load all the words."""
		try:  # try to open file.
			with open(path, "r", encoding="utf-8") as database:
				while not False:
					line = database.readline()
					if not line:
						break
					line = line.rstrip().split(SEPARATOR)
					self._dictionary[line[0]] = line[1:]
				self._len = len(self._dictionary)
				for elt in self._dictionary.items():
					print(elt)
		except FileNotFoundError:  # no file in /database/database.txt.
			try:  # try to open file with backup link.
				self._preload_dictionary(path=BACKUP_DATABASE_PATH)
			except FileNotFoundError:
				pass  # no database yet.

	def run(self) -> None:
		"""load all the words BEFORE starting the application."""
		self._preload_dictionary()

	def get_len(self) -> int:
		"""returns _len."""
		return self._len

	def get_dictionary(self) -> dict:
		"""returns _dictionary."""
		return self._dictionary


class App(Singleton, tkinter.Tk):
	"""main application class."""

	def __new__(cls, *args, **kwargs):
		"""method __new__ of class App."""
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, master=None):
		"""method __init__ of class App."""
		super().__init__(master)
		self._dictionary = Dictionary()
		self._setup_while_startup()

	def _setup_while_startup(self) -> None:
		"""setting settings when starting the application."""
		self._dictionary.run()
		self._main_window_setup()

		self._word_label = self._create_word_label()
		self._translation_label = self._create_translation_label()

		self._next_button = self._create_next_button()
		self._show_button = self._create_show_button()
		self._forgot_button = self._create_forgot_button()

		self._mistakes_text_label = self._create_mistakes_text_label()
		self._mistakes_counter_label = self._create_mistakes_counter_label()

		self._words_text_label = self._create_words_text_label()
		self._words_counter_label = self._create_words_counter_label()

		self._word_text_label = self._create_word_text_label()
		self._word_text = self._create_word_text()

		self._find_button = self._create_find_button()
		self._add_button = self._create_add_button()
		self._edit_button = self._create_edit_button()

		self._transcription_text_label = self._create_transcription_text_label()
		self._transcription_text = self._create_transcription_text()

		self._translation_text_label = self._create_translation_text_label()
		self._translation_text = self._create_translation_text()

		self._result_text_label = self._create_result_text_label()
		self._result_command_label = self._create_result_command_label()

		self._display_interface()

	def _set_keyboard_settings(self, key) -> None:
		"""settings for hot keys."""
		if key.keycode == 86 and key.keysym != 'v':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Paste>>")
		elif key.keycode == 67 and key.keysym != 'c':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Copy>>")
		elif key.keycode == 88 and key.keysym != 'x':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Cut>>")
		elif key.keycode == 65 and key.keysym != 'a':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<SelectAll>>")

	def _main_window_setup(self) -> None:
		"""sets main window settings."""
		self.title(TITLE)
		self.geometry(GEOMETRY)
		self.resizable(False, False)
		self.configure(
			background=BLACK,
			bd=0,
		)
		try:
			self.iconbitmap(ICON_PATH)
		except tkinter.TclError:
			try:
				self.iconbitmap(BACKUP_ICON_PATH)
			except tkinter.TclError:
				pass  # icon didn't load.
		self.bind(KEY_KODE, self._set_keyboard_settings)

	def _create_word_label(self) -> tkinter.Label:
		"""creates a label that will act as a screen for displaying the word."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=NW,
			pady=0,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
		)

	def _create_translation_label(self) -> tkinter.Label:
		"""creates a label that will act as a screen for displaying the word."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=NW,
			pady=0,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
		)

	def _create_next_button(self) -> tkinter.Button:
		"""creates a "NEXT" button which will display a next word from a
			dictionary."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_NEXT_BUTTON,
			command=self._next_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_show_button(self) -> tkinter.Button:
		"""creates a 'SHOW' button that will display the translation of the current
			word."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_SHOW_BUTTON,
			command=self._show_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_forgot_button(self) -> tkinter.Button:
		"""creates a "FORGOT" button which adds a mistake to the mistakes
			counter."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_FORGOT_BUTTON,
			command=self._forgot_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_mistakes_text_label(self) -> tkinter.Label:
		"""creates a "mistakes" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_MISTAKES_COUNTER_LABEL,
		)

	def _create_mistakes_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of incorrect answers."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			foreground=RED,
			text=0,
			font=FONT + BOLD,
		)

	def _create_words_text_label(self) -> tkinter.Label:
		"""creates a "words" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_WORD_LABEL,
		)

	def _create_words_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of words in a dictionary."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			foreground=GREEN,
			text="0" + f"\\{str(self._dictionary.get_len())}",
			font=FONT + BOLD,
		)

	def _create_find_button(self) -> tkinter.Button:
		"""creates a button which finds an existing word in a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_FIND_BUTTON,
			command=self._find_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_add_button(self) -> tkinter.Button:
		"""creates a button which adds a new word to a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_ADD_BUTTON,
			command=self._add_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_edit_button(self) -> tkinter.Button:
		"""creates a button which adds a new word to a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_ADD_BUTTON,
			command=self._edit_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_word_text_label(self) -> tkinter.Label:
		"""creates a "word" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_WORD_LABEL[:-2] + TEXT_WORD_LABEL[-1],
		)

	def _create_word_text(self) -> tkinter.Text:
		"""creates a text field that accepts word transcription."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_transcription_text_label(self) -> tkinter.Label:
		"""creates a "transcription" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_TRANSCRIPTION_LABEL,
		)

	def _create_transcription_text(self) -> tkinter.Text:
		"""creates a text field that accepts word transcription."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_translation_text_label(self) -> tkinter.Label:
		"""creates a "translation" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_TRANSLATION_LABEL,
		)

	def _create_translation_text(self) -> tkinter.Text:
		"""creates a text field that accepts word translation."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_result_text_label(self) -> tkinter.Label:
		"""creates a "result" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_RESULT_LABEL,
		)

	def _create_result_command_label(self) -> tkinter.Label:
		"""creates a "result" label which displays a command result."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_RESULT_COMMAND_LABEL,
		)

	def _next_button_command(self) -> None:
		"""."""
		pass

	def _show_button_command(self) -> None:
		"""."""
		pass

	def _forgot_button_command(self) -> None:
		"""."""
		pass

	def _add_button_command(self) -> None:
		"""."""
		pass

	def _find_button_command(self) -> None:
		"""."""
		pass

	def _edit_button_command(self) -> None:
		"""."""
		pass

	def _display_interface(self) -> None:
		"""shows all interface elements."""
		self._word_label.place(x=5, y=5, width=490, height=50)
		self._translation_label.place(x=5, y=60, width=490, height=50)

		self._next_button.place(x=5, y=115, width=50, height=20)
		self._show_button.place(x=60, y=115, width=50, height=20)
		self._forgot_button.place(x=115, y=115, width=50, height=20)

		self._mistakes_text_label.place(x=170, y=115, width=50, height=20)
		self._mistakes_counter_label.place(x=225, y=115, width=55, height=20)

		self._words_text_label.place(x=285, y=115, width=40, height=20)
		self._words_counter_label.place(x=330, y=115, width=165, height=20)

		self._add_button.place(x=5, y=140, width=50, height=20)
		self._find_button.place(x=60, y=140, width=50, height=20)
		self._edit_button.place(x=115, y=140, width=50, height=20)

		self._word_text_label.place(x=5, y=165, width=75, height=20)
		self._word_text.place(x=85, y=165, width=410, height=20)

		self._transcription_text_label.place(x=5, y=190, width=75, height=20)
		self._transcription_text.place(x=85, y=190, width=410, height=20)

		self._translation_text_label.place(x=5, y=215, width=75, height=20)
		self._translation_text.place(x=85, y=215, width=410, height=20)

		self._result_text_label.place(x=5, y=240, width=75, height=20)
		self._result_command_label.place(x=85, y=240, width=410, height=20)


def main():
	"""main function of the program."""
	App().mainloop()


if __name__ == "__main__":
	main()
