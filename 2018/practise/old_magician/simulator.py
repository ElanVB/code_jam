from bag_memory import BagMemory
from bag import Bag

def unpack_bag(bag, answers):
	if memory.contains(bag):
		return memory.get(bag)

	# print(bag)
	last = bag.check_last()

	if last:
		answers.add(last)
		return

	if bag.black >= 2:
		unpack_bag(bag.take_pair_black(), answers)

	# if bag.white >= 2: # you can't have negative white.... even though you put one back?...
	# 	unpack_bag(bag.take_pair_white(), answers)

	if bag.white >= 1 and bag.black >= 1:
		unpack_bag(bag.take_non_pair(), answers)

if __name__ == "__main__":
	memory = BagMemory()

	with open("A-small-practice.in", "r") as f:
		data = f.readlines()
		T = int(data[0])
		cases = [list(map(int, x.split(" "))) for x in data[1:]]

	for i in range(T):
		starting_bag = Bag(cases[i][1], cases[i][0])

		answers = set()
		unpack_bag(starting_bag, answers)

		if len(answers) > 1:
			answer = "unknown"
		else:
			answer = list(answers)[0]

		memory.add(starting_bag, answer)
		print(answer.upper())
