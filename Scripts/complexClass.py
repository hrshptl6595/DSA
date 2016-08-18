class ComplexNumber:
	"""Represent a complex number."""

	def __init__(self):
		"""Creates a zero complex number"""
		self._real = 0
		self._imag = 0

	def __abs__(self):
		"""Returns the magnitude of the complex number"""
		import math
		return math.sqrt(self._real*self._real + self._imag*self._imag)

	def __add__(self, other):
		"""Returns the addition of two complex numbers"""
		result._real = self._real + other._real
		result._imag = self._imag + other._imag
		return result

	def __sub__(self, other):
		"""Returns the subtraction of two complex numbers"""
		result._real = self._real - other._real
		result._imag = self._imag - other._imag
		return result