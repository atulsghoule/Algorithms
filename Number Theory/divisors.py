def findDivisors(MAXN):
    MAXN+=1
    div = [list() for i in xrange(MAXN+1)]
    for i in xrange(1,MAXN):
        for j in xrange(i,MAXN,i):
            div[j].append(i)
    return div