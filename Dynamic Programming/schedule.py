from random import randint
si=[1,3,0,5,3,5,6,8,8,2,12]
fi=[4,5,6,7,9,9,10,11,12,14,16]
dp={}
# O(n^2)
def schedule(start,end,size):
    ##dynamic programming
    if (start,end,size) in dp:
        return dp[(start,end,size)]
    ##base case
    if size<=0:
        return 0
    ## if compatible
    ans=0
    if si[size-1]>=start and fi[size-1]<=end:
        ## three cases
        # put in first set
        # put in second set
        # dont put
        ans=max(schedule(fi[size-1],end,size-1)+1,
                   schedule(start,si[size-1],size-1)+1,
                   schedule(start,end,size-1))
    else:
        ans=schedule(start,end,size-1)
    dp[(start,end,size)]=ans
    return ans
print schedule(0,float('inf'),len(si))
