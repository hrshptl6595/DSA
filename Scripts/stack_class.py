class stack:
	"""
	Represents a Stack
	"""

	def __init__(self, length = 0):
		"""Initializes the stack"""
		self._stack = [0]*length

	def isEmpty(self):
		"""Checks if the stack is empty or not"""
		if len(self._stack) == 0:
			return True
		else:
			return False

	def push(self, val):
		"""Adds an element to the end of the stack"""
		(self._stack).append(val)
		return self._stack[:]

	def pop(self):
		"""Removes the last element and prints the remaining stack"""
		self._stack = self._stack[:-1]
		return self._stack[:]

	def top(self):
		"""Returns the last element"""
		return self._stack[-1]

	def __str__(self):
		"""String representation of the stack"""
		if len(self._stack) == 0:
			return "Stack is empty"
		else:
			return str(self._stack[:])