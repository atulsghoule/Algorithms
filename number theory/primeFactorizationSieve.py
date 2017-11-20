## program to find prime factorization of a
## number n in O(Log n) time with precomputation allowed
MAXN=13
## stores smallest prime factor for every number
spf=list()


## Calculating SPF (Smallest Prime Factor) for every
## number till MAXN.
## Time Complexity : O(nloglogn)
def sieve():
        global spf
        spf=[i for i in xrange(MAXN)]
        for i in xrange(4,MAXN,2):
            spf[i]=2
        i=3
        while i*i<MAXN:
            if spf[i]==i:
                j=i*i
                while j<MAXN:
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
        
        
    
