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
		if root.dictionary_container.sorted_dictionary:
			root.show_button.configure(state="normal")
			root.right_button.configure(state="normal")
			root.wrong_button.configure(state="normal")
			root.screen_word_label.configure(text="")

			try:
				# TODO: try to fix indents.
				text = "%s\n%s" % (
					root.dictionary_container.sorted_dictionary[
						root.counter][1][3],
					root.dictionary_container.sorted_dictionary[
						root.counter][1][1])
				root.screen_translation_label.configure(text=text)

				root.counter += 1
				root.words_counter_label.configure(
					text=str(root.counter) + "/" + str(len(
						root.dictionary_container.sorted_dictionary)))

			except IndexError:
				root.show_button.configure(state="disabled")
				root.next_button.configure(state="disabled")
				root.right_button.configure(state="disabled")
				root.wrong_button.configure(state="disabled")
				root.screen_word_label.configure(text="")
				root.screen_translation_label.configure(text="")

		else:
			root.show_button.configure(state="disabled")
			root.next_button.configure(state="disabled")
			root.right_button.configure(state="disabled")
			root.wrong_button.configure(state="disabled")
			root.screen_word_label.configure(text="")
			root.screen_translation_label.configure(text="")

	@staticmethod
	def show_command(root: RootWindow):
		"""displays the word and transcription (if available)."""
		root.show_button.configure(state="disabled")

		# TODO: try to fix indents.
		text = """%s\n%s\n%s""" % (
			root.dictionary_container.sorted_dictionary[
				root.counter - 1][0],
			root.dictionary_container.sorted_dictionary[
				root.counter - 1][1][0],
			root.dictionary_container.sorted_dictionary[
				root.counter - 1][1][2])

		root.screen_word_label.configure(text=text)

	@staticmethod
	def right_command(root: RootWindow):
		"""press the button if the answer is correct. the button lowers the
		priority of displaying the current word next time, because the user
		knows this word well."""
		root.right_button.configure(state="disabled")
		root.wrong_button.configure(state="disabled")

		key = root.dictionary_container.sorted_dictionary[
			root.counter - 1][0]
		root.dictionary_container.dictionary[key][4] -= 1

	@staticmethod
	def wrong_command(root: RootWindow):
		"""press the button if the answer is not correct. the button increases
		the priority of displaying the current word next time, because the
		user knows this word poorly."""
		root.right_button.configure(state="disabled")
		root.wrong_button.configure(state="disabled")

		root.mistakes_counter += 1
		root.mistakes_counter_label.configure(text=root.mistakes_counter)

		key = root.dictionary_container.sorted_dictionary[
			root.counter - 1][0]
		root.dictionary_container.dictionary[key][4] += 1

	@staticmethod
	def again_command(root: RootWindow):
		"""starts a new cycle of repeating words."""
		print("5")

	@staticmethod
	def add_command(root: RootWindow):
		"""adds a new word to the dictionary."""
		print("7")

	@staticmethod
	def find_command(root: RootWindow):
		"""finds the word and shows it in the fields."""
		print("8")

	@staticmethod
	def edit_command(root: RootWindow):
		"""edits word's parameters."""
		print("9")

	@staticmethod
	def remove_command(root: RootWindow):
		"""removes word from a dictionary."""
		print("10")

	@staticmethod
	def save_command(root: RootWindow):
		"""saves all the changes in a dictionary to the file."""
		print("6")
