class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

def fractionalKnapsack(W, arr):

	arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
	finalvalue = 0.0
	for item in arr:
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.value
		else:
			finalvalue += item.value * W / item.weight
			break
	return finalvalue

W= 3

arr = [Item(123,12), Item(64, 31), Item(23, 8), Item(33,1), Item(43, 9)]
max_val = fractionalKnapsack(W, arr)
print(max_val)	
