# author: Elan van Biljon
# shared with all those that would like to use it

def increment(items, index, max_index):
	items[index] += 1

	if items[index] > max_index:
		items[index] = items[index-1] + 1
		increment(items, index-1, max_index-1)
		for i in range(index, len(items)):
			items[i] = items[i-1]+1

def n_choose_k(n, k):
	"""
	Feed in a collection of items into n and provide the number of items you
	want to generate unique un-ordered selections from the n items.

	n : list of items to make the selections from
	k: the number of items to select at once
	"""

	assert type(k) == int
	assert type(n) == list

	len_n = len(n)
	indexes = list(range(k))
	final_indexes = list(range(len_n-k, len_n))

	items = []
	while indexes != final_indexes:
		item = [n[i] for i in indexes]
		items.append(item)

		increment(indexes, k-1, len_n-1)

	item = [n[i] for i in indexes]
	items.append(item)
	return items

# I think this can be farther optimized
def n_choose_up_to_k(n, k):
	"""
	Feed in a collection of items into n and provide the number of items you
	want to generate unique un-ordered selections from the [0, n] items.

	n : list of items to make the selections from
	k: the max number of items to select at once
	"""
	items = []
	for current_k in range(0, k+1):
		items += n_choose_k(n, current_k)

	return items

if __name__ == "__main__":
	# items = n_choose_k(list(range(1, 24)), 0)
	items = n_choose_up_to_k(list(range(1, 24)), 2)
	print(items)
	print(len(items))
