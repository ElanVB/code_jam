# import numpy as np # this might not work for google?..

T = int(input())

for t in range(T):
	R, C, H, V = list(map(int, input().split(" ")))

	grid = []
	for r in range(R):
		grid.append([1 if x == "@" else 0 for x in list(input())])

	# grid = np.array(grid)

	# ans = "POSSIBLE"
	ans = "IMPOSSIBLE"

	cumulative_chip_r = [0] * R
	for r in range(R):
		cumulative_chip_r[r] += cumulative_chip_r[max(0, r-1)] + sum(grid[r])

	cumulative_chip_c = [0] * C
	for c in range(C):
		total = 0
		for r in range(R):
			total += grid[r][c]
		cumulative_chip_c[c] += cumulative_chip_c[max(0, c-1)] + total

	# print(grid)

	done = False
	for r in range(R-1):
		if done:
			break

		r_index = r + 1
		for c in range(C-1):
			c_index = c + 1

			pieces = []

			total = 0
			for _r in range(r_index):
				for _c in range(c_index):
					total += grid[_r][_c]
			pieces.append(total)

			total = 0
			for _r in range(r_index, R):
				for _c in range(c_index):
					total += grid[_r][_c]
			pieces.append(total)

			total = 0
			for _r in range(r_index):
				for _c in range(c_index, C):
					total += grid[_r][_c]
			pieces.append(total)

			total = 0
			for _r in range(r_index, R):
				for _c in range(c_index, C):
					total += grid[_r][_c]
			pieces.append(total)

			# print(r, c, pieces)

			_done = False
			for i, p in enumerate(pieces[:-1]):
				# print(p, pieces[i+1])
				if p != pieces[i+1]:
					# print("break")
					_done = False
					break

				_done = True

			if _done:
				done = True
				ans = "POSSIBLE"
				break

			# if len(np.unique(pieces)) == 1:
			# 	ans = "POSSIBLE"
			# 	break

	# ans = "POSSIBLE" if len(np.unique(pieces)) == 1 else "IMPOSSIBLE"

	# print(cumulative_chip_c)
	# print(cumulative_chip_r)

	# if r_possible and c_possible:
	# 	ans = "POSSIBLE"

	print("Case #{}: {}".format(t+1, ans))
