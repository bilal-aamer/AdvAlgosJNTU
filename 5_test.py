from scipy import array,linalg
import pprint

a_ = array([[0, 6, -1, 2, 2, 5],
           [0, 3, 4, 1, 7, 7],
           [5, 1, 0, 3, -1, 2],
           [3, 1, 3, 0, 2, 3],
           [4, 4, 1, -2, 1, 4]])

p,l,u = linalg.lu(a_)

pprint.pprint(p)
pprint.pprint(l)
pprint.pprint(u)