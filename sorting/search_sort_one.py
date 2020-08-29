
items = [1,2,3,4,5,6,7,8,9,10]

def seq_search(items, element):
	pos = 0
	found = False

	while pos < len(items) and not found:

		if items[pos] == element:
			found = True
		else:
			pos += 1  

	return found


def order_seq_search(items, element):
	pos = 0
	found = False
	stopped = False

	while pos < len(items) and not found and not stopped:
		if items[pos] == element:
			found = True
		else:
			if items[pos] > element:
				stopped = True
			else:
				pos += 1

	return found 




#Unordered
print(seq_search(items, 3))

#Ordered
print(order_seq_search(items, 12))
