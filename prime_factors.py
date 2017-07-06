import math
def find_factors(n):
    factor=dict();exp=0
    while n%2 == 0:
        exp+=1
        n = n/2
    ## if divisible by 2 once
    if(exp):
        factor[2]=exp
    ## till square root of num skipping even numbers
    for i in range(3,int(math.sqrt(n))+1,2):
        exp=0
        ## if divisible keep dividing with that number
        while n%i == 0:
            exp+=1
            n = n/i
        ##if divisible once store
        if(exp):
            factor[i]=exp
    ##to check if prime
    if n > 2:
        factor[n]=1
    return factor
