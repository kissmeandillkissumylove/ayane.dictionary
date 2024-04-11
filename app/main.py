"""application launch point."""

from injector import Injector

from app.config import configuration_default
from app.modules.containers import ConfigContainer
from app.modules.file_readers import JsonFileReader
from app.modules.injections_container import MainInjectionContainer
from app.modules.logger import CustomLogger
from app.modules.root_window import RootWindow


def main():
	"""main function which runs the application."""
	_injection_container = Injector([MainInjectionContainer])

	_main_logger = _injection_container.get(CustomLogger)
	_main_logger.log_critical(
		"start the program. init a new logging cycle", _main_logger)

	root_window = _injection_container.get(RootWindow)
	_main_logger.log_debug(
		"create: root_window", root_window)

	root_window.logger = _main_logger

	root_window.injection_container = _injection_container

	json_file_reader = _injection_container.get(JsonFileReader)
	_main_logger.log_debug(
		"create: json_file_reader", json_file_reader)

	current_config = json_file_reader.read_(configuration_default)
	_main_logger.log_debug("read the config file", current_config)

	config_container = _injection_container.get(ConfigContainer)
	_main_logger.log_debug("set: config_container", config_container)

	_main_logger.log_debug(
		"run: set_config(current_config)", config_container)
	config_container.set_config(current_config)

	root_window.configuration = config_container.root_window

	root_window.run()

	_main_logger.log_escape(
		"termination of the program\n%s\n\n" % ("-" * 150))


if __name__ == "__main__":
	main()
