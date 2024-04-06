"""
all the text frames here.
"""
import tkinter
from abc import ABC, abstractmethod
from tkinter import WORD

from injector import singleton

from app.config import GRAY, BLACK, FONT


@singleton
class BaseText(ABC, tkinter.Text):
	"""
	base text for the interface.
	"""

	@abstractmethod
	def _setup_config(self, *args, **kwargs):
		raise NotImplementedError

	def set_position(self, x_pos: int, y_pos: int, width: int, height: int):
		"""
		sets position for the text.
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


class WordText(BaseText):
	"""
	on-screen text field that accepts word.
	"""

	def __init__(self):
		"""
		WordText __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the text.
		"""
		self.configure(
			background=GRAY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD)


class TranscriptionText(BaseText):
	"""
	on-screen text field that accepts word transcription.
	"""

	def __init__(self):
		"""
		TranscriptionText __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the text.
		"""
		self.configure(
			background=GRAY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD)


class TranslationText(BaseText):
	"""
	on-screen text field that accepts word.
	"""

	def __init__(self):
		"""
		TranslationText __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the text.
		"""
		self.configure(
			background=GRAY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD)
