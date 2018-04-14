from bag import Bag

class BagMemory:
	def __init__(self):
		self.memory = dict()

	def add(self, bag, answer):
		self.memory[bag] = answer

	def contains(self, bag):
		return bag in self.memory

	def get(self, bag):
		return self.memory[bag]
