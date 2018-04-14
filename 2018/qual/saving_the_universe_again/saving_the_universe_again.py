T = int(input())

for t in range(T):
	d, pattern = input().split(" ")
	d = int(d)
	pattern = list(pattern)

	# count damage
	total_dammage = 0
	current_charge = 1
	for char in pattern:
		if char == "S":
			total_dammage += current_charge
		elif char == "C":
			current_charge *= 2

	# print(d)
	# print(total_dammage, current_charge)
	ans = 0
	max_index = len(pattern)
	index = max_index - 1
	while index > 0 and total_dammage > d:
		# print(pattern)
		# print(current_charge, total_dammage)

		if pattern[index-1] == "C" and pattern[index] == "S":
			pattern[index] = "C"
			pattern[index-1] = "S"
			# total_dammage += current_charge
			ans += 1
			index = min(index+2, max_index)

			total_dammage = 0
			current_charge = 1
			for char in pattern:
				if char == "S":
					total_dammage += current_charge
				elif char == "C":
					current_charge *= 2
		# elif pattern[index] == "C":
		# 	current_charge /= 2
		# elif pattern[index] == "S":
		# 	total_dammage -= current_charge

		index -= 1

	# if pattern[0] == "S":
	# 	total_dammage -= current_charge

	# print(pattern)
	# print(current_charge, total_dammage)


	if total_dammage > d:
		ans = "IMPOSSIBLE"

	print("Case #{}: {}".format(t+1, ans))
