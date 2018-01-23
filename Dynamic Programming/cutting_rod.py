ans = [1,5,8,9,10,17,17,20,24,30]
n= 10
##dynamic programming cutting rod
for i in xrange(n):
    for j in xrange(i):
        ans[i]=max(ans[j]+ans[i-j-1],ans[i])

