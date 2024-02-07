"""this is my implementation of a dictionary on cards.
02/07/2024 https://github.com/kissmeandillkissumylove"""

# imports
from tkinter import *
from tkinter import ttk


def keypress(e):
	if e.keycode == 86 and e.keysym != 'v':
		widget = main_window.focus_get()
		if isinstance(widget, ttk.Entry) or isinstance(widget, Text):
			widget.event_generate("<<Paste>>")
	elif e.keycode == 67 and e.keysym != 'c':
		widget = main_window.focus_get()
		if isinstance(widget, ttk.Entry) or isinstance(widget, Text):
			widget.event_generate("<<Copy>>")
	elif e.keycode == 88 and e.keysym != 'x':
		widget = main_window.focus_get()
		if isinstance(widget, ttk.Entry) or isinstance(widget, Text):
			widget.event_generate("<<Cut>>")


def add_a_new_word():
	new_word = word_text.get(1.0, "end")
	new_word = new_word.strip()
	new_transcription = transcription_text.get(1.0, "end")
	new_transcription = new_transcription.strip()
	new_translation = translate_text.get(1.0, "end")
	new_translation = new_translation.strip()
	if (len(new_word) - 1) <= 0 and (len(new_translation) - 1) <= 0:
		result_text_label.configure(text="the word and translation fields are too short")
	elif (len(new_word) - 1) <= 0:
		result_text_label.configure(text="the word field is too short")
	elif (len(new_translation) - 1) <= 0:
		result_text_label.configure(text="the translation field is too short")
	else:
		with open("database.txt", "a", encoding="utf-8") as database:
			database.write("@{0}@{1}@{2}@\n".format(
				new_word, new_transcription, new_translation))

# settings
main_window = Tk()
main_window.geometry("300x320+400+200")
main_window.resizable(False, False)
main_window.title("ᴋɪssᴍᴇᴀɴᴅɪʟʟᴋɪssᴜᴍʏʟöᴠᴇ")
try:
	main_window.iconbitmap("icon.ico")
except:
	pass

main_window.configure(
	background="black",
	bd=0,
)

screen_label = Label(
	master=main_window,
	background="#B5B5B5",
	bd=0,
)

start_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="sᴛᴀʀᴛ",
	foreground="white",
	bd=2,
)

next_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="ɴᴇxᴛ",
	foreground="white",
	bd=2,
)

show_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="sʜᴏᴡ",
	foreground="white",
	bd=2,
)

forgot_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="ꜰᴏʀɢᴏᴛ",
	foreground="white",
	bd=2,
)

mistakes_count_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴍɪsᴛᴀᴋᴇs ᴄᴏᴜɴᴛ:",
	fg="white",
)

mistakes_counter_label = Label(
	master=main_window,
	background="black",
	bd=0,
	font="verdana 8 bold",
	text="0",
	fg="red",
)

words_passed_count_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴡᴏʀᴅs ᴘᴀssᴇᴅ ᴄᴏᴜɴᴛ:",
	fg="white",
)

words_counter_label = Label(
	master=main_window,
	background="black",
	bd=0,
	font="verdana 8 bold",
	text="0",
	fg="green",
)

add_a_new_word_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="ᴀᴅᴅ ᴀ ɴᴇᴡ ᴡᴏʀᴅ",
	foreground="white",
	bd=2,
	command=add_a_new_word,
)

word_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴡᴏʀᴅ:",
	fg="white",
)

word_text = Text(
	master=main_window,
	fg="black",
	bg="#B5B5B5",
	wrap=WORD,
	font="verdana 8",
	bd=0,
)

transcription_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴛʀᴀɴsᴄʀɪᴘᴛɪᴏɴ:",
	fg="white",
)

transcription_text = Text(
	master=main_window,
	fg="black",
	bg="#B5B5B5",
	wrap=WORD,
	font="verdana 8",
	bd=0,
)

translate_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴛʀᴀɴsʟᴀᴛɪᴏɴ:",
	fg="white",
)

translate_text = Text(
	master=main_window,
	fg="black",
	bg="#B5B5B5",
	wrap=WORD,
	font="verdana 8",
	bd=0,
)

result_of_the_operation_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ʀᴇsᴜʟᴛ:",
	fg="white",
)

result_text_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="the fields are empty",
	fg="white",
	font="verdana 7",
)

screen_label.place(x=5, y=5, width=290, height=150)
start_button.place(x=5, y=162, width=70, height=25)
next_button.place(x=80, y=162, width=70, height=25)
show_button.place(x=155, y=162, width=70, height=25)
forgot_button.place(x=230, y=162, width=65, height=25)
mistakes_count_label.place(x=5, y=190, width=90, height=15)
mistakes_counter_label.place(x=100, y=190, width=35, height=15)
words_passed_count_label.place(x=140, y=190, width=110, height=15)
words_counter_label.place(x=255, y=190, width=40, height=15)
add_a_new_word_button.place(x=5, y=210, width=290, height=25)
word_label.place(x=5, y=240, width=75, height=15)
word_text.place(x=85, y=240, width=210, height=15)
transcription_label.place(x=5, y=260, width=75, height=15)
transcription_text.place(x=85, y=260, width=210, height=15)
translate_label.place(x=5, y=280, width=75, height=15)
translate_text.place(x=85, y=280, width=210, height=15)
result_of_the_operation_label.place(x=5, y=300, width=50, height=15)
result_text_label.place(x=60, y=300, width=235, height=15)

main_window.bind("<Control-KeyPress>", keypress)

main_window.mainloop()
