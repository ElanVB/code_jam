import random

with open("big.in", "w") as f:
	f.write("100\n")
	for _ in range(100):
		moves = []
		for _ in range(30):
			if random.random() < 0.5:
				moves.append("S")
			else:
				moves.append("C")

		f.write("{} {}\n".format(int(random.random() * 10**2), "".join(moves)))
