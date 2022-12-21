from itertools import permutations

# n = int(input('Enter number of jobs '))
n =2

# graph = []

# for i in range(n):
#  row = []
#  for j in range(n):
#     inp = int(input(f'Enter cost for person {i+1} to do the job {j+1} '))
#     row.append(inp)
#  graph.append(row)

graph = [[2,3],[4,2]]


l = list(permutations(range(n)))
print("Permutation iter: ",l)

min = 1000000
index = -1

for i in l:
 t = 0
 for j in range(n):
    t += graph[i[j]][j]
 if t < min:
    min = t
    index = i

print(f'Min cost is {min}')
print(f'Job index is {index}')