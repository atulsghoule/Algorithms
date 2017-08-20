## mo's algorithm
from math import sqrt
##array
array=[1,2,3,4,5,6,7,8,9]
query=[[1,9],[2,1],[3,1],[7,1],[4,1]]
##defining the block size sqrt(n)
block=int(sqrt(len(array)))
##comparision function
def compare(a,b):
    if(a[0]/block!=b[0]/block):
        return int(a[0]/block>b[0]/block)-1
    else:
        return int(a[1]>b[1])-1
##sorting the query array on the basis of the function
query.sort(compare)
'''
 solve the problem as normal
'''
