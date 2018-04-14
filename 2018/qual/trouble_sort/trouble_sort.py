T = int(input())

for t in range(T):
	n = input()
	L = list(map(int, input().split(" ")))

	# sort
	# print(L)
	done = False
	while not done:
		done = True
		for i in range(len(L)-2):
			if L[i] > L[i+2]:
				done = False
				temp = L[i]
				L[i] = L[i+2]
				L[i+2] = temp

	in_order = True
	for i, num in enumerate(L[:-1]):
		if L[i] > L[i+1]:
			in_order = False
			break

	if in_order:
		print("Case #{}: OK".format(t+1))
	else:
		print("Case #{}: {}".format(t+1, i))
