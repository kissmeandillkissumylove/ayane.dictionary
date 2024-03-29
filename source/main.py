import tkinter


class App(tkinter.Tk):
	"""
	main application class. creates main window.
	"""

	def __new__(cls, *args, **kwargs):
		"""
		method __new__ of App class. calls Singleton __new__.
		:param args:  arguments passed when creating a class.
		:param kwargs: named arguments passed when creating a class.
		"""
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, master=None):
		"""
		method __init__ of App class. creates new App object.
		:param master: screen. None by default.
		"""
		super().__init__(master)


def main():
	"""
	main function. runs application.
	"""
	app = App(config=)
	app.mainloop()


if __name__ == "__main__":
	main()
