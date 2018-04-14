T = int(input())
for t in range(T):
	a = int(input())
	y = list(range(2, int(a/3) + 1, 2))
	y_len = len(y)

	done = False
	index = 0
	while not done:
		print("2 {}".format(y[index]))
		index = (index + 1) % y_len

		r_in, c_in = list(map(int, input().split(" ")))
		if r_in == c_in == 0:
			done = True
