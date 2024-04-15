"""contains button commands container."""

from app.modules.base_structures import BaseFuncContainer


class CommandsContainer(BaseFuncContainer):
	"""consists of button commands."""

	@staticmethod
	def next_command():
		"""the "next" button will randomly show the next word from the
		dictionary."""
		print("1")
