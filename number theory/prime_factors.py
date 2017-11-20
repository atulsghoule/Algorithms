import math
def find_factors(n):
    factor=dict();exp=0
    for i in range(2,int(math.sqrt(n))+1):
        exp=0
        while n%i == 0:
            exp+=1
            n = n/i
        if(exp):
            factor[i]=exp
    if n > 1:
        factor[n]=1
    return factor
