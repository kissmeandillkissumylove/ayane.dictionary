"""it's an implementation of dictionary on cards by ayane miuro
02/07/2024 https://github.com/kissmeandillkissumylove"""
import tkinter
from tkinter import NW, W

from constants import *


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


class App(Singleton, tkinter.Tk):
	"""main application class."""

	def __init__(self, master=None):
		"""method __init__ of class Singleton."""
		super().__init__(master)
		self._setup_while_startup()

	def _setup_while_startup(self):
		"""setting settings when starting the application."""
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

		self._display_interface()

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
			pass  # icon didn't load

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
		)

	def _create_mistakes_text_label(self) -> tkinter.Label:
		"""creates a "mistakes" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=BLUE,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_MISTAKES_COUNTER_LABEL,
		)

	def _create_mistakes_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of incorrect answers."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=999999,
			font=FONT + BOLD,
		)

	def _create_words_text_label(self) -> tkinter.Label:
		"""creates a "words" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=BLUE,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_WORD_LABEL,
		)

	def _create_words_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of words in a dictionary."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text="999998/999999",
			font=FONT + BOLD,
		)

	def _create_result_text_label(self) -> tkinter.Label:

	def _next_button_command(self) -> None:
		"""."""
		pass

	def _show_button_command(self) -> None:
		"""."""
		pass

	def _forgot_button_command(self) -> None:
		"""."""
		pass

	def _display_interface(self) -> None:
		"""shows all interface elements."""
		self._word_label.place(x=5, y=5, width=490, height=50)
		self._translation_label.place(x=5, y=60, width=490, height=50)
		self._next_button.place(x=5, y=115, width=50, height=25)
		self._show_button.place(x=60, y=115, width=50, height=25)
		self._forgot_button.place(x=115, y=115, width=50, height=25)
		self._mistakes_text_label.place(x=170, y=115, width=50, height=25)
		self._mistakes_counter_label.place(x=220, y=115, width=60, height=25)
		self._words_text_label.place(x=285, y=115, width=40, height=25)
		self._words_counter_label.place(x=325, y=115, width=170, height=25)


def main():
	"""main function of the program."""
	App().mainloop()


if __name__ == "__main__":
	main()
