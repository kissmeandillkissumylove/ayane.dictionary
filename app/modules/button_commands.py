"""contains button commands container."""
import tkinter

from app.modules.base_structures import BaseFuncContainer
from app.modules.root_window import RootWindow


class CommandsContainer(BaseFuncContainer):
	"""consists of button commands."""

	@staticmethod
	def next_command(root: RootWindow):
		"""the "next" button will randomly show the next word from the
		dictionary."""
		print("1")

	@staticmethod
	def show_command(root: tkinter.Tk):
		"""displays the word and transcription (if available)."""
		print("2")

	@staticmethod
	def right_command(root: tkinter.Tk):
		"""press the button if the answer is correct. the button lowers the
		priority of displaying the current word next time, because the user
		knows this word well."""
		print("3")

	@staticmethod
	def wrong_command(root: tkinter.Tk):
		"""press the button if the answer is not correct. the button increases
		the priority of displaying the current word next time, because the
		user knows this word poorly."""
		print("4")

	@staticmethod
	def again_command(root: tkinter.Tk):
		"""starts a new cycle of repeating words."""
		print("5")

	@staticmethod
	def add_command(root: tkinter.Tk):
		"""adds a new word to the dictionary."""
		print("7")

	@staticmethod
	def find_command(root: tkinter.Tk):
		"""finds the word and shows it in the fields."""
		print("8")

	@staticmethod
	def edit_command(root: tkinter.Tk):
		"""edits word's parameters."""
		print("9")

	@staticmethod
	def remove_command(root: tkinter.Tk):
		"""removes word from a dictionary."""
		print("10")

	@staticmethod
	def save_command(root: tkinter.Tk):
		"""saves all the changes in a dictionary to the file."""
		print("6")
