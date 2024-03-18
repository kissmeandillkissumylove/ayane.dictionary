"""it's an implementation of dictionary on cards by ayane miuro
02/07/2024 https://github.com/kissmeandillkissumylove"""
import tkinter
from tkinter import NW

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
		self.items = {}

	def _setup_while_startup(self):
		"""setting settings when starting the application."""
		self.title(TITLE)
		try:
			self.iconbitmap(ICON_PATH)
		except tkinter.TclError:
			# icon didn't load
			pass
		self.geometry(GEOMETRY)
		self.resizable(False, False)
		self.configure(
			background=BLACK,
			bd=0,
		)
		self._create_and_display_word_label()

	def _create_and_display_word_label(self) -> None:
		"""returns label that will act as a screen for displaying the word."""
		tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=NW,
			pady=0,
			padx=2,
			wraplength=286,
			justify="left",
			foreground=BLACK,
		).place(x=5, y=5, width=490, height=50)


def main():
	"""main function of the program."""
	App().mainloop()


if __name__ == "__main__":
	main()
