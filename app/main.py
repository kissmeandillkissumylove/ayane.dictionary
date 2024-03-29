import tkinter
from dataclasses import dataclass
from typing import Union


@dataclass
class ValidationTypes:
	geometry = Union[str, None]
	background = Union[str, None]
	title = Union[str, None]
	icon = Union[str, None]


@dataclass
class ValidationPatterns:
	geometry: Union[str, None] = r"^(\\d+)x(\\d+)(?:\\+\\d+)?(?:\\+\\d+)?$"
	background: Union[str, None] = r"^#[0-9a-fA-F]{6}$",
	title: Union[str, None] = r"^.{0,32}$",
	icon: Union[str, None] = None


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
				- background (str): background color (e.g., "#ffffff", "#2D81B2").
				- title (str): the title of the application window.
				- icon (str or pathlib.Path): path to the application icon.
		"""
		super().__init__()


def main():
	"""
	main function. runs application.
	"""
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()
