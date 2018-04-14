def increment(items, index, max_index):
	items[index] += 1

	if items[index] > max_index:
		items[index] = items[index-1] + 1
		increment(items, index-1, max_index-1)
		for i in range(index, len(items)):
			items[i] = items[i-1]+1

def n_choose_k(n, k):
	assert type(k) == int
	assert type(n) == list

	len_n = len(n)
	indexes = list(range(k))
	final_indexes = list(range(len_n-k, len_n))

	items = []
	while indexes != final_indexes:
		# numpy items.append([n[indexes]])
		item = [n[i] for i in indexes]
		items.append(item)

		increment(indexes, k-1, len_n-1)

	item = [n[i] for i in indexes]
	items.append(item)
	return items

if __name__ == "__main__":
	items = n_choose_k(list(range(1, 27)), 13)
	print(len(items))
	# print(items)
