"""all the basic structures are collected here."""
import logging
import tkinter
from abc import abstractmethod, ABC
from dataclasses import dataclass

import injector
from injector import Binder


class BaseInjectionContainer(injector.Module):
	"""abstract class to represent an injection container."""

	@abstractmethod
	def configure(self, binder: Binder) -> None:
		"""contains injections and the rules by which injections are
		introduced."""
		raise NotImplementedError


class BaseWindow(ABC, tkinter.Tk):
	"""abstract class to represent a window."""

	def __init__(self):
		"""BaseWindow __init__."""
		super().__init__()

	@abstractmethod
	def _setup_configuration(self, *args, **kwargs):
		"""sets window configuration."""
		raise NotImplementedError


class BaseFileReader(ABC):
	"""abstract class for reading a file."""

	@abstractmethod
	def read_(self, *args, **kwargs):
		"""reads the file."""
		raise NotImplementedError


@dataclass
class BaseValidator(ABC):
	"""abstract class for data validation."""

	@staticmethod
	@abstractmethod
	def validate(*args, **kwargs) -> bool:
		"""validates the data.
		:return: boolean."""
		raise NotImplementedError


class BaseLogger(ABC, logging.Logger):
	"""abstract class for logger."""

	@abstractmethod
	def _setup_logger(self, *args, **kwargs):
		"""sets settings for the logger."""
		raise NotImplementedError
