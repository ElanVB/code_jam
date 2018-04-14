import numpy as np, sys

T = int(input())
for t in np.arange(T):
	lower, upper = map(int, input().split(" "))
	N = int(input())
	p = int((lower + upper) / 2)

	done = False
	while not done:
		print(p)
		# print(p, file=sys.stderr)
		feedback = input().upper()

		if feedback == "CORRECT":
			done = True
		elif feedback == "TOO_SMALL":
			lower = p
		elif feedback == "TOO_BIG":
			upper = p
		else:
			sys.exit(-1)
		p = int((lower + upper) / 2)
