def get_n(t):
	ms = []
	for c in cashiers:
		m = int((t - c[2])/c[1])
		n = min(m, c[0])
		# print(t, c, n)

		if n > 0:
			ms.append(n)

	# ms = list(filter(lambda x: x != 0, ms))
	ms.sort()
	ms = ms[::-1]
	# print(ms)
	# print(sum(ms))
	# print(sum(ms[:R]))

	return sum(ms[:R])

T = int(input())

for t in range(T):
	R, B, C = list(map(int, input().split(" ")))

	cashiers = []
	max_t = 0
	for c in range(C):
		cashiers.append(list(map(int, input().split(" "))))

		_t = cashiers[c][0]*cashiers[c][1] + cashiers[c][2]

		if _t > max_t:
			max_t = _t

	ans = max_t

	lower = 0
	upper = max_t

	prev = 0
	current = int((upper + lower)/2)

	done = False
	while not done:
		n = get_n(current)

		# print (B, current, n)

		if n >= B:
			ans = current
			upper = current
		else:
			lower = current

		current = int((upper + lower)/2)

		if current == prev:
			done = True

		prev = current

	print("Case #{}: {}".format(t+1, ans))
