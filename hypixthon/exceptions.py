# coding=utf-8

class APIError(Exception):
	def __init__(self, message):
		self.message = message
		Exception.__init__(self, self.message)

	def __str__(self):
		return self.message

class ArgumentException(Exception):
	def __init__(self, message):
		self.message = message
		Exception.__init__(self, self.message)

	def __str__(self):
		return self.message
