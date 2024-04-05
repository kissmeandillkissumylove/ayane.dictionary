"""
all the labels are here.
"""
import tkinter
from abc import ABC, abstractmethod
from tkinter import NW

from injector import singleton

from app.config import GRAY, BLACK, FONT


@singleton
class BaseLabel(ABC, tkinter.Label):
	"""
	base label for the interface.
	"""

	@abstractmethod
	def _setup_config(self, *args, **kwargs):
		raise NotImplementedError


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
