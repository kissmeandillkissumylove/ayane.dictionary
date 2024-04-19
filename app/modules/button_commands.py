"""contains button commands container."""

from app.modules.base_structures import BaseFuncContainer


class CommandsContainer(BaseFuncContainer):
	"""consists of button commands."""

	@staticmethod
	def next_command():
		"""the "next" button will randomly show the next word from the
		dictionary."""
		print("1")

	@staticmethod
	def show_command():
		"""displays the word and transcription (if available)."""
		print("2")

	@staticmethod
	def right_command():
		"""press the button if the answer is correct. the button lowers the
		priority of displaying the current word next time, because the user
		knows this word well."""
		print("3")

	@staticmethod
	def wrong_command():
		"""press the button if the answer is not correct. the button increases
		the priority of displaying the current word next time, because the
		user knows this word poorly."""
		print("4")

	@staticmethod
	def again_command():
		"""starts a new cycle of repeating words."""
		print("5")

	@staticmethod
	def save_command():
		"""saves all the changes in a dictionary to the file."""
		print("6")

	@staticmethod
	def add_command():
		"""adds a new word to the dictionary."""
		print("7")

	@staticmethod
	def find_command():
		"""finds the word and shows it in the fields."""
		print("8")

	@staticmethod
	def edit_command():
		"""edits word's parameters."""
		print("9")
