"""application launch point."""

from injector import Injector

from app.config import configuration_default
from app.modules.containers import ConfigContainer
from app.modules.file_readers import JsonFileReader
from app.modules.injections_container import MainInjectionContainer
from app.modules.logger import CustomLogger
from app.modules.root_window import RootWindow


def set_app_configuration(
		logger: CustomLogger,
		injection_container: Injector,
		root_window: RootWindow,
		path: str = configuration_default):
	"""sets configuration for the app."""
	logger.log_debug("run: set_app_configuration()", path)

	if not isinstance(logger, CustomLogger):
		raise TypeError("wrong type for the logger.")

	if not isinstance(injection_container, Injector):
		logger.log_critical(
			"try: _injection_container", injection_container)
		raise TypeError("wrong type for the _injection_container.")

	if not isinstance(root_window, RootWindow):
		logger.log_critical(
			"try: root_window", root_window)
		raise TypeError("wrong type for the root_window.")

	json_file_reader = injection_container.get(JsonFileReader)
	logger.log_debug(
		"create: json_file_reader", json_file_reader)

	current_config = json_file_reader.read_(path)
	logger.log_debug("read the config file", current_config)

	config_container = injection_container.get(ConfigContainer)
	logger.log_debug("set: config_container", config_container)

	logger.log_debug(
		"run: set_config(current_config)", config_container)
	config_container.set_config(current_config)

	root_window.configuration = config_container.root_window


def main():
	"""main function which runs the application."""
	_injection_container = Injector([MainInjectionContainer])

	_main_logger = _injection_container.get(CustomLogger)
	_main_logger.log_critical(
		"start the program. init a new logging cycle", _main_logger)

	root_window = _injection_container.get(RootWindow)
	_main_logger.log_debug(
		"create: root_window", root_window)

	set_app_configuration(
		_main_logger, _injection_container, root_window)

	root_window.run()

	_main_logger.log_escape(
		"termination of the program\n%s\n\n" % ("-" * 150))


if __name__ == "__main__":
	main()
