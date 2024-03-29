"""it's an implementation of dictionary on cards by ayane miuro.
02/07/2024 - 03/18/2024 https://github.com/kissmeandillkissumylove"""
from constants import *
from dataclasses import dataclass, field
import datetime
import random
import tkinter
from tkinter import NW, W, WORD, ttk


class Singleton(object):
	"""singleton implementation."""
	_instance = None

	def __new__(cls, *args, **kwargs):
		"""method __new__ of class Singleton."""
		if not isinstance(cls._instance, cls):
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def __del__(self):
		"""method __del__ of class Singleton."""
		Singleton._instance = None


@dataclass
class Dictionary(Singleton):
	"""a dataclass used to store all the words."""
	_dictionary: dict = field(default_factory=dict)
	_len: int = 0

	def _preload_dictionary(self, path=DATABASE_PATH) -> None:
		"""load all the words."""
		try:  # try to open file.
			with open(path, "r", encoding="utf-8") as database:
				while not False:
					line = database.readline()
					if not line:
						break
					line = line.rstrip().split(SEP)
					self._dictionary[line[0]] = line[1:]
				self._len = len(self._dictionary)

		except FileNotFoundError:  # no file in /database/database.txt.
			if path != BACKUP_DATABASE_PATH:
				# try to open file with backup link.
				self._preload_dictionary(path=BACKUP_DATABASE_PATH)

	def run(self) -> None:
		"""load all the words BEFORE starting the application."""
		self._preload_dictionary()

	def get_len(self) -> int:
		"""returns _len."""
		return self._len

	def get_dictionary(self) -> dict:
		"""returns _dictionary."""
		return self._dictionary

	def set_new_values(
			self,
			key: str,
			transcription: str = "",
			translation: str = "",
			counter: str = ""
	) -> None:
		"""sets a new value for the key."""
		if counter == "":
			if key in self._dictionary:
				self._dictionary[key] = [
					self._dictionary[key][0] if transcription == "" else transcription,
					self._dictionary[key][1] if translation == "" else translation,
					self._dictionary[key][2],
					self._dictionary[key][3],
					self._dictionary[key][4],
				]

			else:
				self._dictionary[key] = [
					transcription,
					translation,
					str(datetime.date.today()),
					"0",
					"0",
				]

		else:
			temp = [
				self._dictionary[key][0],
				self._dictionary[key][1],
				self._dictionary[key][2],
				self._dictionary[key][3],
				self._dictionary[key][4]
			]

			temp[4] = str(int(temp[4]) + int(counter))
			if temp[4] == "3":
				temp[4] = "0"
				temp[3] = str(int(temp[3]) + 1)
			elif temp[4] == "-3":
				temp[4] = "0"
				temp[3] = str(int(temp[3]) - 1)

			if temp[3] == "0":
				pass
			elif int(temp[3]) > 0:
				temp[2] = str(datetime.date.today() + datetime.timedelta(
					days=int(temp[3])))
			elif int(temp[3]) < 0:
				temp[2] = str(datetime.date.today())

			self._dictionary[key] = temp

	def print_dictionary(self) -> None:
		"""prints all the words with keys and values."""
		print("-" * 80)
		for item in self._dictionary.items():
			print(f"{item[0]} : {item[1]}")
		print("-" * 80)

	def save_changes(self, path=DATABASE_PATH) -> None:
		"""saves all the changes in a dictionary to the file."""
		try:  # try to open file.
			with open(path, "w", encoding="utf-8") as database:
				for _ in self._dictionary.items():
					database.write(
						_[0] + SEP
						+ _[1][0] + SEP
						+ _[1][1] + SEP
						+ _[1][2] + SEP
						+ _[1][3] + SEP
						+ _[1][4] + "\n"
					)

		except FileNotFoundError:  # no file in /database/database.txt.
			if path != BACKUP_DATABASE_PATH:
				# try to open file with backup link.
				self.save_changes(path=BACKUP_DATABASE_PATH)


class App(Singleton, tkinter.Tk):
	"""main application class."""

	def __new__(cls, *args, **kwargs):
		"""method __new__ of class App."""
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, master=None):
		"""method __init__ of class App."""
		super().__init__(master)
		self._dictionary = Dictionary()
		self._setup_while_startup()

	def _setup_while_startup(self) -> None:
		"""setting settings when starting the application."""
		self._prepare_dictionary()
		self._main_window_setup()

		self._word_label = self._create_word_label()
		self._translation_label = self._create_translation_label()

		self._next_button = self._create_next_button()
		self._show_button = self._create_show_button()
		self._right_button = self._create_right_button()
		self._wrong_button = self._create_wrong_button()
		self._again_button = self._create_again_button()
		self._save_button = self._create_save_button()

		self._mistakes_text_label = self._create_mistakes_text_label()
		self._mistakes_counter_label = self._create_mistakes_counter_label()

		self._words_text_label = self._create_words_text_label()
		self._words_counter_label = self._create_words_counter_label()

		self._word_text_label = self._create_word_text_label()
		self._word_text = self._create_word_text()

		self._find_button = self._create_find_button()
		self._add_button = self._create_add_button()
		self._edit_button = self._create_edit_button()

		self._transcription_text_label = self._create_transcription_text_label()
		self._transcription_text = self._create_transcription_text()

		self._translation_text_label = self._create_translation_text_label()
		self._translation_text = self._create_translation_text()

		self._result_text_label = self._create_result_text_label()
		self._result_command_label = self._create_result_command_label()

		self._display_interface()

	def _set_keyboard_settings(self, key) -> None:
		"""settings for hot keys."""
		if key.keycode == 86 and key.keysym != 'v':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Paste>>")
		elif key.keycode == 67 and key.keysym != 'c':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Copy>>")
		elif key.keycode == 88 and key.keysym != 'x':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<Cut>>")
		elif key.keycode == 65 and key.keysym != 'a':
			widget = self.focus_get()
			if isinstance(widget, ttk.Entry) or isinstance(widget, tkinter.Text):
				widget.event_generate("<<SelectAll>>")

	def _prepare_dictionary(self) -> None:
		"""load all the words BEFORE starting the application."""
		self._dictionary.run()
		self._prepare_copy_dictionary()

	def _prepare_copy_dictionary(self):
		"""prepares the dictionary to refresh today's words."""
		self._prepared_dictionary = {}

		for _ in self._dictionary.get_dictionary().items():
			if _[1][2] <= str(datetime.date.today()):
				self._prepared_dictionary[_[0]] = _[1]

		self._keys_prepared_dictionary = list(self._prepared_dictionary.keys())
		self._text_word_counter = f"\\{len(
			self._prepared_dictionary)}\\{self._dictionary.get_len()}"
		self._counter = 0
		self._mistakes_counter = 0

	def _main_window_setup(self) -> None:
		"""sets main window settings."""
		self.title(TITLE)
		self.geometry(GEOMETRY)
		self.resizable(False, False)
		self.configure(
			background=BLACK,
			bd=0,
		)
		try:
			self.iconbitmap(ICON_PATH)
		except tkinter.TclError:
			try:
				self.iconbitmap(BACKUP_ICON_PATH)
			except tkinter.TclError:
				pass  # icon didn't load.
		self.bind(KEY_KODE, self._set_keyboard_settings)

	def _get_words_counter_label_text(self, text: int = 0) -> str:
		"""returns text for "words counter" label"""
		return str(text) + self._text_word_counter

	def _create_word_label(self) -> tkinter.Label:
		"""creates a label that will act as a screen for displaying the word."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=NW,
			pady=0,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
		)

	def _create_translation_label(self) -> tkinter.Label:
		"""creates a label that will act as a screen for displaying the word."""
		return tkinter.Label(
			master=self.master,
			background=GREY,
			bd=0,
			anchor=NW,
			pady=0,
			padx=2,
			wraplength=486,
			justify="left",
			foreground=BLACK,
		)

	def _create_next_button(self) -> tkinter.Button:
		"""creates a "NEXT" button which will display a next word from a
			dictionary."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_NEXT_BUTTON,
			command=self._next_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_show_button(self) -> tkinter.Button:
		"""creates a 'SHOW' button that will display the translation of the current
			word."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_SHOW_BUTTON,
			command=self._show_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_right_button(self) -> tkinter.Button:
		"""creates a "RIGHT" button which performs actions if the answer is correct"""
		return tkinter.Button(
			master=self.master,
			background=LIME,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_RIGHT_BUTTON,
			command=self._right_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_wrong_button(self) -> tkinter.Button:
		"""creates a "WRONG" button which performs actions if the answer is
			incorrect."""
		return tkinter.Button(
			master=self.master,
			background=LIME,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_WRONG_BUTTON,
			command=self._wrong_button_command,
			state="disabled",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_again_button(self) -> tkinter.Button:
		"""creates an "AGAIN" button which restarts a revision cycle."""
		return tkinter.Button(
			master=self.master,
			background=RED,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_AGAIN_BUTTON,
			command=self._again_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_save_button(self) -> tkinter.Button:
		"""creates a "SAVE" button which saves all the changes to database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_BLUE,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_SAVE_BUTTON,
			command=self._save_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_mistakes_text_label(self) -> tkinter.Label:
		"""creates a "mistakes" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_MISTAKES_COUNTER_LABEL,
		)

	def _create_mistakes_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of incorrect answers."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			foreground=RED,
			text=0,
			font=FONT + BOLD,
		)

	def _create_words_text_label(self) -> tkinter.Label:
		"""creates a "words" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_WORD_LABEL,
		)

	def _create_words_counter_label(self) -> tkinter.Label:
		"""creates a label which will count the number of words in a dictionary."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			foreground=GREEN,
			text=self._get_words_counter_label_text(),
			font=FONT + BOLD,
		)

	def _create_find_button(self) -> tkinter.Button:
		"""creates a button which finds an existing word in a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_FIND_BUTTON,
			command=self._find_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_add_button(self) -> tkinter.Button:
		"""creates a button which adds a new word to a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_ADD_BUTTON,
			command=self._add_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_edit_button(self) -> tkinter.Button:
		"""creates a button which adds a new word to a database."""
		return tkinter.Button(
			master=self.master,
			background=DARK_GREEN,
			bd=2,
			foreground=WHITE,
			activebackground=BLUE,
			text=TEXT_EDIT_BUTTON,
			command=self._edit_button_command,
			state="normal",
			disabledforeground=ALMOST_BLACK,
		)

	def _create_word_text_label(self) -> tkinter.Label:
		"""creates a "word" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_WORD_LABEL[:-2] + TEXT_WORD_LABEL[-1],
		)

	def _create_word_text(self) -> tkinter.Text:
		"""creates a text field that accepts word transcription."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_transcription_text_label(self) -> tkinter.Label:
		"""creates a "transcription" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_TRANSCRIPTION_LABEL,
		)

	def _create_transcription_text(self) -> tkinter.Text:
		"""creates a text field that accepts word transcription."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_translation_text_label(self) -> tkinter.Label:
		"""creates a "translation" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_TRANSLATION_LABEL,
		)

	def _create_translation_text(self) -> tkinter.Text:
		"""creates a text field that accepts word translation."""
		return tkinter.Text(
			master=self.master,
			background=GREY,
			bd=0,
			foreground=BLACK,
			font=FONT,
			wrap=WORD,
		)

	def _create_result_text_label(self) -> tkinter.Label:
		"""creates a "result" label just for text."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_RESULT_LABEL,
		)

	def _create_result_command_label(self) -> tkinter.Label:
		"""creates a "result" label which displays a command result."""
		return tkinter.Label(
			master=self.master,
			background=ALMOST_BLACK,
			bd=0,
			anchor=W,
			foreground=WHITE,
			text=TEXT_RESULT_COMMAND_LABEL,
		)

	def _next_button_command(self) -> None:
		"""the "next" button will randomly show the next word from the dictionary."""
		if self._keys_prepared_dictionary:
			self._counter += 1

			self._show_button.configure(state="normal")
			self._right_button.configure(state="normal")
			self._wrong_button.configure(state="normal")
			self._word_label.configure(text="")

			self._words_counter_label.configure(
				text=self._get_words_counter_label_text(self._counter))

			self._current_key = random.choice(self._keys_prepared_dictionary)
			self._keys_prepared_dictionary.remove(self._current_key)
			self._current_item = self._prepared_dictionary.pop(self._current_key)

			self._translation_label.configure(text=self._current_item[1])
		else:
			self._show_button.configure(state="disabled")
			self._next_button.configure(state="disabled")
			self._right_button.configure(state="disabled")
			self._wrong_button.configure(state="disabled")
			self._word_label.configure(text="")
			self._translation_label.configure(text="")

			self._word_label.configure(background=RED)

	def _show_button_command(self) -> None:
		"""displays the word and transcription (if available)."""
		text = self._current_key + "\n" + self._current_item[0]
		self._word_label.configure(text=text)
		self._show_button.configure(state="disabled")

	def _right_button_command(self) -> None:
		"""press the button if the answer is correct. the button lowers the priority of
			displaying the current word next time, because the user knows this word
			well."""
		self._right_button.configure(state="disabled")
		self._wrong_button.configure(state="disabled")
		self._dictionary.set_new_values(key=self._current_key, counter="1")

	def _wrong_button_command(self) -> None:
		"""press the button if the answer is not correct. the button increases the
			priority of displaying the current word next time, because the user knows
			this word poorly."""
		self._right_button.configure(state="disabled")
		self._wrong_button.configure(state="disabled")

		self._mistakes_counter += 1
		self._mistakes_counter_label.configure(text=self._mistakes_counter)

		self._dictionary.set_new_values(key=self._current_key, counter="-1")

	def _again_button_command(self) -> None:
		"""starts a new cycle of repeating words."""
		self._again_button.configure(state="disabled")

		if not self._keys_prepared_dictionary:
			self._prepare_copy_dictionary()
			self._translation_label.configure(text=TEXT_OUT_OF_WORDS)

			self._next_button.configure(state="normal")

			self._word_label.configure(background=GREY)
			self._words_counter_label.configure(
				text=self._get_words_counter_label_text())
			self._mistakes_counter_label.configure(text=0)

		else:
			self._show_button.configure(state="disabled")
			self._right_button.configure(state="disabled")
			self._wrong_button.configure(state="disabled")
			self._translation_label.configure(text=TEXT_PREPARE_NEW_DICTIONARY)
			self._word_label.configure(background=GREY, text="")
			self._words_counter_label.configure(
				text=self._get_words_counter_label_text())
			self._mistakes_counter_label.configure(text=0)
			self._prepare_copy_dictionary()

		self._again_button.configure(state="normal")

	def _save_button_command(self) -> None:
		"""saves all the changes in a dictionary to the file."""
		self._save_button.configure(state="disabled")
		self._dictionary.save_changes()
		self._save_button.configure(state="normal")
		self._result_command_label.configure(text=SAVED)

	def _add_button_command(self) -> None:
		"""adds a new word to the dictionary."""
		new_word = self._word_text.get(1.0, "end").strip()

		if new_word not in self._dictionary.get_dictionary():
			new_transcription = self._transcription_text.get(1.0, "end").strip()
			new_translation = self._translation_text.get(1.0, "end").strip()

			if len(new_word) <= 0 and len(new_translation) <= 0:
				self._result_command_label.configure(text=BOTH_FIELDS_EMPTY)

			elif (len(new_word)) <= 0:
				self._result_command_label.configure(text=WORD_FiELD_EMPTY)

			elif len(new_translation) <= 0:
				self._result_command_label.configure(text=TRANSL_FiELD_EMPTY)

			else:
				self._dictionary.set_new_values(
					key=new_word,
					transcription=new_transcription,
					translation=new_translation
				)
				self._result_command_label.configure(text=WORD_ADDED)
				self._word_text.delete(1.0, "end")
				self._transcription_text.delete(1.0, "end")
				self._translation_text.delete(1.0, "end")

		else:
			self._word_text.delete(1.0, "end")
			self._transcription_text.delete(1.0, "end")
			self._translation_text.delete(1.0, "end")
			self._result_command_label.configure(text=WORD_EXISTS)

	def _find_button_command(self) -> None:
		"""finds the word and shows it in the fields."""
		word = self._word_text.get(1.0, "end").strip()

		if word in self._dictionary.get_dictionary():
			self._transcription_text.delete(1.0, "end")
			self._translation_text.delete(1.0, "end")
			self._transcription_text.insert(
				1.0, self._dictionary.get_dictionary()[word][0]
			)
			self._translation_text.insert(
				1.0, self._dictionary.get_dictionary()[word][1]
			)
			self._result_command_label.configure(text="")

		else:
			self._word_text.delete(1.0, "end")
			self._transcription_text.delete(1.0, "end")
			self._translation_text.delete(1.0, "end")
			self._result_command_label.configure(text=NO_WORD)

	def _edit_button_command(self) -> None:
		"""edits word's parameters."""
		word = self._word_text.get(1.0, "end").strip()

		if word in self._dictionary.get_dictionary():
			self._dictionary.set_new_values(
				key=word,
				transcription=self._transcription_text.get(1.0, "end").strip(),
				translation=self._translation_text.get(1.0, "end").strip()
			)
			self._word_text.delete(1.0, "end")
			self._transcription_text.delete(1.0, "end")
			self._translation_text.delete(1.0, "end")
			self._result_command_label.configure(text=EDITED)

		else:
			self._word_text.delete(1.0, "end")
			self._transcription_text.delete(1.0, "end")
			self._translation_text.delete(1.0, "end")
			if word == "":
				self._result_command_label.configure(text=WORD_FiELD_EMPTY)
			else:
				self._result_command_label.configure(text=NO_WORD)

	def _display_interface(self) -> None:
		"""shows all interface elements."""
		self._word_label.place(x=5, y=5, width=490, height=50)
		self._translation_label.place(x=5, y=60, width=490, height=50)

		self._next_button.place(x=5, y=115, width=50, height=20)
		self._show_button.place(x=60, y=115, width=50, height=20)
		self._right_button.place(x=115, y=115, width=50, height=20)
		self._wrong_button.place(x=170, y=115, width=50, height=20)
		self._again_button.place(x=225, y=115, width=50, height=20)
		self._save_button.place(x=280, y=115, width=50, height=20)

		self._mistakes_text_label.place(x=170, y=140, width=50, height=20)
		self._mistakes_counter_label.place(x=225, y=140, width=55, height=20)
		self._words_text_label.place(x=285, y=140, width=40, height=20)
		self._words_counter_label.place(x=330, y=140, width=165, height=20)

		self._add_button.place(x=5, y=140, width=50, height=20)
		self._find_button.place(x=60, y=140, width=50, height=20)
		self._edit_button.place(x=115, y=140, width=50, height=20)

		self._word_text_label.place(x=5, y=165, width=75, height=20)
		self._word_text.place(x=85, y=165, width=410, height=20)

		self._transcription_text_label.place(x=5, y=190, width=75, height=20)
		self._transcription_text.place(x=85, y=190, width=410, height=20)

		self._translation_text_label.place(x=5, y=215, width=75, height=20)
		self._translation_text.place(x=85, y=215, width=410, height=20)

		self._result_text_label.place(x=5, y=240, width=75, height=20)
		self._result_command_label.place(x=85, y=240, width=410, height=20)


def main():
	"""main function of the program."""
	App().mainloop()


if __name__ == "__main__":
	main()
