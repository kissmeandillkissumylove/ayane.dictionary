"""all the basic structures are collected here."""
import abc
import tkinter

import injector
from injector import Binder


class BaseInjectionContainer(injector.Module):
	"""abstract class to represent an injection container."""

	@abc.abstractmethod
	def configure(self, binder: Binder) -> None:
		"""contains injections and the rules by which injections are
		introduced."""
		raise NotImplementedError


class BaseWindow(abc.ABC, tkinter.Tk):
	"""abstract class to represent a window."""

	def __init__(self):
		"""BaseWindow __init__."""
		super().__init__()

	@abc.abstractmethod
	def _setup_configuration(self, *args, **kwargs):
		"""sets window configuration."""
		raise NotImplementedError
