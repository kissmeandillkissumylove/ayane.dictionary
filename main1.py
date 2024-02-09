"""this is my implementation of a dictionary on cards.
02/07/2024 https://github.com/kissmeandillkissumylove"""

# imports
from tkinter import *
from tkinter import ttk
import random

ddc = {}
word, word_data = "", []
ddc_len, counter, mistakes = "0", 0, 0


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


def start():
	with open("database.txt", "r", encoding="utf-8") as database:
		while True:
			line = database.readline()
			if not line:
				break
			line = line.split("@")
			ddc[line[0]] = [line[1], line[2]]
			global ddc_len
		ddc_len = str(len(ddc))
	words_counter_label.configure(text="0/" + ddc_len)


def nextt():
	try:
		global counter, ddc_len
		counter += 1
		show_button.configure(state="normal")
		forgot_button.configure(state="normal")
		words_counter_label.configure(text=str(counter) + "/" + ddc_len)
		screen_label1.configure(background="#B5B5B5", foreground="#B5B5B5")
		word = random.choice(list(ddc.keys()))
		word_data = ddc.pop(word)
		screen_label1.configure(text=word + "\n" + word_data[0])
		screen_label2.configure(text=word_data[1])
	except IndexError:
		counter = 0
		screen_label1.configure(text="", background="red")
		screen_label2.configure(
			text="all the words are over. a new list for repeating words is ready.")
		start()
		show_button.configure(state="disabled")
		forgot_button.configure(state="disabled")
		global mistakes
		mistakes = 0
		mistakes_counter_label.configure(text="0")


def showw():
	screen_label1.configure(foreground="black")
	show_button.configure(state="disabled")


def forgott():
	forgot_button.configure(state="disabled")
	global mistakes
	mistakes += 1
	mistakes_counter_label.configure(text=str(mistakes))


def add_a_new_word():
	new_word = word_text.get(1.0, "end")
	new_word = new_word.strip()
	if new_word not in ddc.keys():
		new_transcription = transcription_text.get(1.0, "end")
		new_transcription = new_transcription.strip()
		new_translation = translate_text.get(1.0, "end")
		new_translation = new_translation.strip()
		if (len(new_word)) <= 0 and (len(new_translation)) <= 0:
			result_text_label.configure(text="the word and translation fields are too short.")
		elif (len(new_word)) <= 0:
			result_text_label.configure(text="the word field is too short.")
		elif (len(new_translation)) <= 0:
			result_text_label.configure(text="the translation field is too short.")
		else:
			with open("database.txt", "a", encoding="utf-8") as database:
				database.write("{0}@{1}@{2}\n".format(
					new_word, new_transcription, new_translation))
			result_text_label.configure(text="the new word added successfully.")
			word_text.delete(1.0, "end")
			transcription_text.delete(1.0, "end")
			translate_text.delete(1.0, "end")
			screen_label1.configure(background="red", text="")
			screen_label2.configure(text="you added a new word. the repetition will begin again.")
			show_button.configure(state="disabled")
			forgot_button.configure(state="disabled")
			global mistakes, counter
			mistakes, counter = 0, 0
			mistakes_counter_label.configure(text="0")
			words_counter_label.configure(text="0")
			start()
	else:
		word_text.delete(1.0, "end")
		transcription_text.delete(1.0, "end")
		translate_text.delete(1.0, "end")
		result_text_label.configure(text="this word is already in the dictionary.")


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

screen_label1 = Label(
	master=main_window,
	background="#B5B5B5",
	bd=0,
	anchor=NW,
	pady=0,
	padx=2,
	wraplength=286,
	justify="left",
)

screen_label2 = Label(
	master=main_window,
	background="#B5B5B5",
	bd=0,
	anchor=NW,
	pady=0,
	padx=2,
	wraplength=286,
	justify="left",
	foreground="black"
)

next_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="ɴᴇxᴛ",
	foreground="white",
	bd=2,
	command=nextt,
)

show_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="sʜᴏᴡ",
	foreground="white",
	bd=2,
	command=showw,
	state="disabled"
)

forgot_button = Button(
	master=main_window,
	background="#DF1313",
	activebackground="#2D81B2",
	text="ꜰᴏʀɢᴏᴛ",
	foreground="white",
	bd=2,
	command=forgott,
	state="disabled"
)

mistakes_count_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴍɪsᴛᴀᴋᴇs:",
	fg="white",
)

mistakes_counter_label = Label(
	master=main_window,
	background="black",
	bd=0,
	font="verdana 8 bold",
	text="0",
	fg="red",
	anchor=W,
)

words_passed_count_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴡᴏʀᴅs:",
	fg="white",
)

words_counter_label = Label(
	master=main_window,
	background="black",
	bd=0,
	font="verdana 8 bold",
	text="0",
	fg="green",
	anchor=W,
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
	text="the fields are empty.",
	fg="white",
	font="verdana 7",
)

screen_label1.place(x=5, y=5, width=290, height=75)
screen_label2.place(x=5, y=85, width=290, height=70)
next_button.place(x=5, y=162, width=95, height=25)
show_button.place(x=105, y=162, width=95, height=25)
forgot_button.place(x=205, y=162, width=90, height=25)
mistakes_count_label.place(x=5, y=190, width=50, height=15)
mistakes_counter_label.place(x=60, y=190, width=40, height=15)
words_passed_count_label.place(x=105, y=190, width=40, height=15)
words_counter_label.place(x=150, y=190, width=145, height=15)
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
start()

main_window.mainloop()
