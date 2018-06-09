T = int(input())

for t in range(T):
	x, y = list(map(int, input().split(" ")))

	ans = x + y
	print("Case #{}: {}".format(t+1, ans))
