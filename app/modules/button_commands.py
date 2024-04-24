"""contains button commands container."""

from app.config import (
	PREPARE_NEW_DICTIONARY, WORD_EXISTS, INDENT_MESSAGE,
	BOTH_FIELDS_EMPTY, WORD_FIELD_EMPTY, TRANSL_FIELD_EMPTY,
	WORD_ADDED, NO_SUCH_WORD)
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
		root.again_button.configure(state="disabled")
		root.screen_word_label.configure(text="")
		root.screen_translation_label.configure(text="")
		root.show_button.configure(state="disabled")
		root.right_button.configure(state="disabled")
		root.wrong_button.configure(state="disabled")
		root.next_button.configure(state="normal")

		if root.dictionary_container.dictionary is not None:
			root.dictionary_container.new_revise_cycle()
			root.reset_all_the_counters()

			root.screen_translation_label.configure(
				text=PREPARE_NEW_DICTIONARY)

			root.words_counter_label.configure(text="%s/%s" % (
				root.counter, len(root.dictionary_container.dictionary)))
			root.mistakes_counter_label.configure(text=0)

		root.again_button.configure(state="normal")

	@staticmethod
	def add_command(root: RootWindow):
		"""adds a new word to the dictionary."""
		new_word = root.word_text.get(1.0, "end").strip()

		if "\n" in new_word:
			root.clear_all_the_fields()
			root.command_label.configure(text=INDENT_MESSAGE)

		if new_word not in root.dictionary_container.dictionary:
			new_transcription = root.transcription_text.get(
				1.0, "end").strip()
			new_part_of_speech = root.part_of_speech_text.get(
				1.0, "end").strip()
			new_usage_example = root.usage_example_text.get(
				1.0, "end").strip()
			new_translation = root.translation_text.get(
				1.0, "end").strip()

			if (
					"\n" in new_transcription) or (
					"\n" in new_part_of_speech) or (
					"\n" in new_usage_example) or (
					"\n" in new_translation):
				root.clear_all_the_fields()
				root.command_label.configure(text=INDENT_MESSAGE)

			if len(new_word) <= 0 and len(new_translation) <= 0:
				root.command_label.configure(text=BOTH_FIELDS_EMPTY)

			elif (len(new_word)) <= 0:
				root.command_label.configure(text=WORD_FIELD_EMPTY)

			elif len(new_translation) <= 0:
				root.command_label.configure(text=TRANSL_FIELD_EMPTY)

			else:
				root.dictionary_container.dictionary[new_word] = [
					new_transcription,
					new_part_of_speech,
					new_usage_example,
					new_translation,
					0]

				root.clear_all_the_fields()
				root.command_label.configure(text=WORD_ADDED)

		else:
			root.clear_all_the_fields()
			root.command_label.configure(text=WORD_EXISTS)

	@staticmethod
	def find_command(root: RootWindow):
		"""finds the word and shows it in the fields."""
		word = root.word_text.get(1.0, "end").strip()

		if word in root.dictionary_container.dictionary:
			root.clear_all_the_fields()

			word_data = root.dictionary_container.dictionary[word]
			root.word_text.insert(1.0, word)
			root.transcription_text.insert(1.0, word_data[0])
			root.part_of_speech_text.insert(1.0, word_data[1])
			root.usage_example_text.insert(1.0, word_data[2])
			root.translation_text.insert(1.0, word_data[3])

			root.command_label.configure(text="")

		else:
			root.clear_all_the_fields()
			root.command_label.configure(text=NO_SUCH_WORD)

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
