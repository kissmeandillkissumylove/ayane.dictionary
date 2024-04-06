"""
all the buttons are here.
"""
import tkinter
from abc import ABC, abstractmethod

from injector import singleton

from app.config import (
	RED, WHITE, BLUE, NEXT_BUTTON, ALMOST_BLACK, SHOW_BUTTON,
	LIME, RIGHT_BUTTON, WRONG_BUTTON, AGAIN_BUTTON, SAVE_BUTTON,
	DARK_BLUE, DARK_GREEN, ADD_BUTTON, FIND_BUTTON, EDIT_BUTTON)


@singleton
class BaseButton(ABC, tkinter.Button):
	"""
	base label for the interface.
	"""

	@abstractmethod
	def _setup_config(self, *args, **kwargs):
		raise NotImplementedError

	@abstractmethod
	def _command(self, *args, **kwargs):
		raise NotImplementedError

	def set_position(self, x_pos: int, y_pos: int, width: int, height: int):
		"""
		sets position for the label.
		:param x_pos: int.
		:param y_pos: int.
		:param width: int.
		:param height: int.
		"""
		if (
				type(x_pos) is int and type(y_pos) is int and
				type(width) is int and type(height) is int
		):
			self.place(x=x_pos, y=y_pos, width=width, height=height)
		else:
			raise tkinter.TclError(f"{self.__class__.__name__} set_position")


class NextButton(BaseButton):
	"""
	a button which will display a next word from a dictionary.
	"""

	def __init__(self):
		"""
		NextButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=RED,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=NEXT_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		the "next" button will randomly show the next word from the
		dictionary.
		"""
		pass


class ShowButton(BaseButton):
	"""
	a "show" button that will display the translation of the current word.
	"""

	def __init__(self):
		"""
		ShowButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=RED,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=SHOW_BUTTON,
			bd=2,
			command=self._command,
			state="disabled")

	def _command(self):
		"""
		the "next" button will display the word and transcription (if available).
		"""
		pass


class RightButton(BaseButton):
	"""
	a "wight" button which performs actions if the answer is correct.
	"""

	def __init__(self):
		"""
		RightButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=LIME,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=RIGHT_BUTTON,
			bd=2,
			command=self._command,
			state="disabled")

	def _command(self):
		"""
		press the button if the answer is correct. the button lowers the
		priority of displaying the current word next time, because the user
		knows this word well.
		"""
		pass


class WrongButton(BaseButton):
	"""
	a "wrong" button which performs actions if the answer is incorrect.
	"""

	def __init__(self):
		"""
		RightButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=LIME,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=WRONG_BUTTON,
			bd=2,
			command=self._command,
			state="disabled")

	def _command(self):
		"""
		press the button if the answer is not correct. the button increases
		the priority of displaying the current word next time, because the
		user knows this word poorly.
		"""
		pass


class AgainButton(BaseButton):
	"""
	an "again" button which restarts a revision cycle.
	"""

	def __init__(self):
		"""
		AgainButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=RED,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=AGAIN_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		starts a new cycle of repeating words.
		"""
		pass


class SaveButton(BaseButton):
	"""
	a "save" button which saves all the changes to database.
	"""

	def __init__(self):
		"""
		SaveButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=DARK_BLUE,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=SAVE_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		saves all the changes in a dictionary.
		"""
		pass


class AddButton(BaseButton):
	"""
	a "add" button which adds a new word to a database.
	"""

	def __init__(self):
		"""
		AddButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=DARK_GREEN,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=ADD_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		adds a new word to the dictionary.
		"""
		pass


class FindButton(BaseButton):
	"""
	a "find" button which finds an existing word in a database.
	"""

	def __init__(self):
		"""
		FindButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=DARK_GREEN,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=FIND_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		finds the word and shows it in the fields.
		"""
		pass


class EditButton(BaseButton):
	"""
	a "edit" button which edits the translation and transcription fields of
	a word.
	"""

	def __init__(self):
		"""
		EditButton __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the button.
		"""
		self.configure(
			background=DARK_GREEN,
			foreground=WHITE,
			activebackground=BLUE,
			disabledforeground=ALMOST_BLACK,
			text=EDIT_BUTTON,
			bd=2,
			command=self._command,
			state="normal")

	def _command(self):
		"""
		edits word's parameters.
		"""
		pass
