import pprint
MAX = 100


def luDecomposition(mat, n):

	lower = [[0 for x in range(n)]
			for y in range(n)]
	upper = [[0 for x in range(n)]
			for y in range(n)]
 
	for i in range(n):

		# Upper Triangular
		for k in range(i, n):
			sum = 0
			for j in range(i):
				sum += (lower[i][j] * upper[j][k])
			upper[i][k] = mat[i][k] - sum

		# Lower Triangular
		for k in range(i, n):
			if (i == k):
				lower[i][i] = 1 
			else:
				sum = 0
				for j in range(i):
					sum += (lower[k][j] * upper[j][i])
				lower[k][i] = int((mat[k][i] - sum)/upper[i][i])

	print("Lower Triangular")
	pprint.pprint(lower)

	print("Upper Triangular")
	pprint.pprint(upper)


mat = [[2, -1, -2],
	[-4, 6, 3],
	[-4, -2, 8]]

luDecomposition(mat, 3)

# This code is contributed by mits
