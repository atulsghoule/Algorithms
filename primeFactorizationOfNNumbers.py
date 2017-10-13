## program to find prime factorization of a
## number n in O(Log n) time with precomputation allowed
MAXN=10**7
## stores smallest prime factor for every number
## marking smallest prime factor for every
## number to be itself.
spf=[i for i in xrange(MAXN)]

## Calculating SPF (Smallest Prime Factor) for every
## number till MAXN.
## Time Complexity : O(nloglogn)
def sieve():
        ## separately marking spf for every even
        ## number as 2
        for i in xrange(4,MAXN,2):
            spf[i]=2
        i=3
        while i*i<MAXN:
            ## checking if i is prime
            if spf[i]==i:
                ## marking SPF for all numbers divisible by i
                j=i*i
                while j<MAXN:
                    ## marking spf[j] if it is not 
                    ## previously marked
                    if spf[j]==j:
                        spf[j]=i
                    j+=i
                    
            i+=1
## A O(log n) function returning primefactorization
## by dividing by smallest prime factor at every step
def getFactorization(x):
    ans=list()
    while x!=1:
        ans.append(spf[x])
        x=x/spf[x]
    return ans
        
        
    
