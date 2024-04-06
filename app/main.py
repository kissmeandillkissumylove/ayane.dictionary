"""application launch point."""

from injector import Injector

from app.modules.injections_container import MainInjectionContainer
from app.modules.root_window import RootWindow


def main():
	"""main function which runs the application."""
	_injection_container = Injector([MainInjectionContainer])

	root_window = _injection_container.get(RootWindow)
	root_window.injection_container = _injection_container

	root_window.run()


if __name__ == "__main__":
	main()
