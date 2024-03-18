"""it's an implementation of dictionary on cards by ayane miuro
02/07/2024 https://github.com/kissmeandillkissumylove"""
import tkinter

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
		self.title(TITLE)
		self.geometry(GEOMETRY)
		self.resizable(False, False)


def main():
	"""main function of the program."""
	App().mainloop()


if __name__ == "__main__":
	main()
