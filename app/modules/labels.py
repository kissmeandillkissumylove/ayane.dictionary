"""
all the labels are here.
"""
import tkinter
from abc import ABC, abstractmethod
from tkinter import NW, W

from injector import singleton

from app.config import (
	GRAY, BLACK, FONT, ALMOST_BLACK, WHITE, MISTAKES_TEXT_LABEL,
	RED, BOLD, WORDS_LABEL, GREEN, RESULT_LABEL,
	TRANSCRIPTION_LABEL, TRANSLATION_LABEL)


@singleton
class BaseLabel(ABC, tkinter.Label):
	"""
	base label for the interface.
	"""

	@abstractmethod
	def _setup_config(self, *args, **kwargs):
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


class ScreenWordLabel(BaseLabel):
	"""
	on-screen label that is needed to display a word in a foreign language.
	"""

	def __init__(self):
		"""
		ScreenWordLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=GRAY,
			bd=0,
			anchor=NW,
			pady=2,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
			font=FONT)


class ScreenTranslationLabel(BaseLabel):
	"""
	on-screen label that is needed to display a current word translation.
	"""

	def __init__(self):
		"""
		ScreenTranslationLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=GRAY,
			bd=0,
			anchor=NW,
			pady=2,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
			font=FONT)


class MistakesTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		MistakesTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=MISTAKES_TEXT_LABEL)


class MistakesCounterLabel(BaseLabel):
	"""
	on-screen label which will count the number of incorrect answers.
	"""

	def __init__(self):
		"""
		MistakesCounterLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			text=0,
			foreground=RED,
			font=FONT + BOLD)


class WordsTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		WordsTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=WORDS_LABEL)


class WordsCounterLabel(BaseLabel):
	"""
	on-screen label which will count the number of words in a dictionary.
	"""

	def __init__(self):
		"""
		WordsCounterLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			text="0/0",
			foreground=GREEN,
			font=FONT + BOLD)


class WordTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		WordTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=WORDS_LABEL[:-2] + WORDS_LABEL[-1])


class TranscriptionTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		TranscriptionTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TRANSCRIPTION_LABEL)


class TranslationTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		TranslationTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TRANSLATION_LABEL)


class ResultTextLabel(BaseLabel):
	"""
	on-screen label just for text.
	"""

	def __init__(self):
		"""
		ResultTextLabel __init__.
		"""
		super().__init__()
		self._setup_config()

	def _setup_config(self):
		"""
		sets configure for the label.
		"""
		self.configure(
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=RESULT_LABEL)
