class BaseValidation:
	"""
	base class for data validation.
	"""

	def validate(self, value):
		"""
		base function for data validation.
		"""
		raise NotImplementedError


class StringValidation(BaseValidation):
	"""
	class for the string validation.
	"""

	def validate(self, value) -> bool:
		"""
		function for the string validation.
		:param value: data.
		:return: boolean.
		"""
		return isinstance(value, str)


class NoneValidation(BaseValidation):
	"""
	class for the None validation.
	"""

	def validate(self, value) -> bool:
		"""
		function for the None validation.
		:param value: data.
		:return: boolean.
		"""
		return True if value else False
