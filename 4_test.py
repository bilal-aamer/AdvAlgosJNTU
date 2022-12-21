import numpy as np
import sys
 
# n = int(input('Enter number of unknowns: '))


# a = np.zeros((n,n+1))
# x = np.zeros(n) 

# print('Enter Augmented Matrix Coefficients:')

# for i in range(n):
#     for j in range(n+1):
#         a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

a = [[1, 1, 1, 1, 1],[1, 2, 3, 4, 2],[1, 3, 6, 10, 3],[1, 4, 10, 20, 4]]


a_ = np.array([[0, 6, -1, 2, 2],
           [0, 3, 4, 1, 7],
           [5, 1, 0, 3, -1],
           [3, 1, 3, 0, 2],
           [4, 4, 1, -2, 1]], float)
b_ = np.array([5, 7, 2, 3, 4], float)

n = len(a_)

if(n == len(a_)):
    x = np.linalg.solve(a_,b_)
else:
    for i in range(n):
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
 
print('\nThe solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')