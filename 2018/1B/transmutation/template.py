class Node:
	def __init__(self, _id, value, left, right):
		self.id = _id
		self.value = value
		self.left = left
		self.right = right

	def make(self):
		if self.left and self.right:
			num = min(self.left.value, self.right.value)
			self.value += num
			self.left.reduce(num)
			self.right.reduce(num)

	def reduce(self, num):
		self.value -= num

	def sum(self): # these trees are infinitely deep... so this won't work...
		total = 0
		if self.left:
			total += self.left.sum()

		if self.right:
			total += self.right.sum()

		return total

	def ord_child(self):
		if self.left and self.right:
			if self.left.value < self.right.value:
				return [self.left, self.right]
			elif self.right.value < self.left.value:
				return [self.right, self.left]
			else:
				return [self.left, self.right]
		else:
			(None, )

	def __repr__(self):
		if self.left:
			l = self.left.id
		else:
			l = None

		if self.right:
			r = self.right.id
		else:
			r = None

		return "id: {}, val: {}, l: {}, r: {}".format(
			self.id, self.value, l, r
		)

class Tree:
	def __init__(self, root):
		self.root = root

	def value(self):
		return self.root.value

	def make(self):
		self._make(self.root)

	def _make(self, node):
		node.make()

		for child in node.ord_child():
			self._make(child)

	# def prune(self):
	# 	self._prune(self.root)

	# def _prune(self, node): # you might as well prune both...
	# 	if node.left_min_prop() == 0 or node.right_min_prop() == 0:
	# 		node.left = None
	# 		node.right = None
	# 	else:

T = int(input())

for t in range(T):
	M = int(input())
	recipies = []
	for m in range(M):
		left, right = list(map(int, input().split(" ")))
		recipies.append([left, right])

	values = list(map(int, input().split(" ")))

	# make nodes
	nodes = []
	for m in range(M):
		nodes.append(Node(m, values[m], None, None))

	# link nodes
	for i, [left, right] in enumerate(recipies):
		if left != 1 and right != 1:
			nodes[i].left = nodes[left-1]
			nodes[i].right = nodes[right-1]

	print(nodes)

	root = Tree(nodes[0])
	root.make()

	print("Case #{}: {}".format(t+1, root.value()))
