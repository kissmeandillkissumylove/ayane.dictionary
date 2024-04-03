from unittest.mock import Mock


def reset_mocks(func):
	"""
	reset all the mocks after test case.
	:param func: test_func.
	:return: wrapper.
	"""

	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)

		for arg in args:
			if isinstance(arg, Mock):
				arg.reset_mock()

		return result

	return wrapper
