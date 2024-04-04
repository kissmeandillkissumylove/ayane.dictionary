class ConfigNotFoundError(Exception):
	"""
	configuration file not found.
	"""

	def __init__(self, message="configuration file not found"):
		self.message = message
		super().__init__(self.message)
