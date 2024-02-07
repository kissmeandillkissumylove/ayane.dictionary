"""this is my implementation of a dictionary on cards.
02/07/2024 https://github.com/kissmeandillkissumylove"""

# imports
from tkinter import *
from tkinter import ttk

# settings
main_window = Tk()
main_window.geometry("300x300+400+200")
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

translate_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="ᴛʀᴀɴsʟᴀᴛᴇ:",
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
	text="ʀᴇsᴜʟᴛ ᴏꜰ ᴛʜᴇ ᴏᴘᴇʀᴀᴛɪᴏɴ:",
	fg="white",
)

result_text_label = Label(
	master=main_window,
	background="black",
	bd=0,
	text="example",
	fg="white",
	font="verdana 8",
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
word_label.place(x=5, y=240, width=55, height=15)
word_text.place(x=65, y=240, width=230, height=15)
translate_label.place(x=5, y=260, width=55, height=15)
translate_text.place(x=65, y=260, width=230, height=15)
result_of_the_operation_label.place(x=5, y=280, width=125, height=15)
result_text_label.place(x=135, y=280, width=160, height=15)

main_window.mainloop()
