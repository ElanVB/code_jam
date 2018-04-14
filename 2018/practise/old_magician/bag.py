class Bag:
	def __init__(self, black, white):
		if black < 0 or white < 0:
			raise Exception("both white and black must be non-negative.")
		self.black = black
		self.white = white

	def take_pair_black(self):
		return Bag(self.black-2, self.white+1)

	def take_pair_white(self):
		return Bag(self.black, self.white-1)

	def take_non_pair(self):
		return Bag(self.black, self.white-1)

	def check_last(self):
		if self.black + self.white == 1:
			return "black" if self.black else "white"

		return False

	def __repr__(self):
		return "{} {}".format(self.black, self.white)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
		 	return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash(self.__repr__())
