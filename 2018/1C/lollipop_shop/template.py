import random, math

T = int(input())

for t in range(T):
	N = int(input())

	p = [1/N] * N
	for n in range(N):
		data = list(map(int, input().split(" ")))
		D = data[0]
		flavs = data[1:]

		min_p = math.inf
		min_flav = -1
		min_set = []
		for flav in flavs:
			if p[flav] > 0:
				if (p[flav] < min_p):
					min_p = p[flav]
					min_flav = flav
					min_set = [flav]
				elif p[flav] == min_p:
					min_set.append(flav)

			p[flav] *= 2 # try make this more maths-ey

		if len(min_set) > 1:
			min_flav = random.choice(min_set)

		if min_flav > -1:
			p[min_flav] = 0

		print(min_flav)
