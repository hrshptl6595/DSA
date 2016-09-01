class Stack(object):
	"""A simple stack ADT with top as the end of a list"""
	def __init__(self):
		self.items = []

	def __str__(self):
		return ("Stack of size: %d" % len(self.items))

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def top(self):
		if self.isEmpty():
			return None
		return self.items[len(self.items)-1]

def match_paren(parens):
	"""returns true or false if parenthesis expression passed is matching"""
	stack = Stack()
	for b in parens:
		if b == "(":
			stack.push(1)
		elif b == ")":
			if not stack.isEmpty():
				stack.pop()
			else:
				return False
	return stack.isEmpty()

if __name__ == "__main__":
	print(match_paren("1+(2*3*(4/6*(5+6)))"))