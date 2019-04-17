## Eulers Totient Function
from math import sqrt
def totient(num):
    result = num
    for p in xrange(2,int(sqrt(num))+1):
        if num%p == 0:
            while num%p==0:
                num/=p
            result -= result/p
    if num!=1:
        result -= result/num
    return result

## Pillai's arithmetical function
def pill(num):
    result = 0
    for i in xrange(1,int(sqrt(num))+1):
        if num%i==0:
            result+= i*totient(num/i)
            if i!= num/i:
                result+= (num/i)*totient(i)
    return result

## Eulers Totient Function using sieve
def totientSieve(size):
    size+=1
    toti = [i for i in xrange(size)]
    for i in xrange(2,size):
        if toti[i] == i:
            toti[i]  = i - 1
            for j in xrange(2*i,size,i):
                toti[j] -= (toti[j] / i)
    return toti

## Pillai's arithmetical function sieve
def pillSieve(size):
    size+=1
    toti = totientSieve(size)
    totiS = [0]* size
    for i in xrange(1,size):
        k = 1
        for j in xrange(i,size,i):
            totiS[j] += i*toti[k]
            k+=1
    return totiS



