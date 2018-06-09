import math

T = int(input())

for t in range(T):
	N = int(input())
	w = list(map(int, input().split(" ")))

	back_i = 0

	while back_i < len(w):
		ants = w[:-back_i-1]

		strength = 6 * w[-back_i-1]
		weight = sum(ants)
		diff = weight - strength

		if diff > 0:
			candidates = []
			indexes = []
			for i, ant in enumerate(ants):
				x = diff - ant

				if x <= 0:
					candidates.append(x)
					indexes.append(i)

			if len(candidates) == 0:
				del(w[-back_i-1])
			else:
				min_candidate_index = None
				min_candidate = math.inf

				for i, candidate in enumerate(candidates):
					if candidate <= min_candidate:
						min_candidate = candidate
						min_candidate_index = indexes[i]

				del(w[min_candidate_index])

		back_i += 1

	ans = len(w)
	print("Case #{}: {}".format(t+1, ans))
