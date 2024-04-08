"""application launch point."""

from injector import Injector

from app.config import configuration_default
from app.modules.file_readers import JsonFileReader
from app.modules.injections_container import MainInjectionContainer
from app.modules.logger import CustomLogger
from app.modules.root_window import RootWindow


def main():
	"""main function which runs the application."""
	_injection_container = Injector([MainInjectionContainer])
	_logger_ = _injection_container.get(CustomLogger)
	_logger_.set_logger_level(10)
	_logger_.log(50, "start new logging cycle.")

	root_window = _injection_container.get(RootWindow)
	root_window.injection_container = _injection_container

	json_file_reader = _injection_container.get(JsonFileReader)
	current_config = json_file_reader.read_(configuration_default)
	root_window.configuration_dict = current_config

	root_window.run()
	_logger_.log(50, "termination of the program. stop logging.\n\n")


if __name__ == "__main__":
	main()
