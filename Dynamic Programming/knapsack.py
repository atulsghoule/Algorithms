##knapsack problem

##solution First
dp={}
def knap(capacity,length):
    if (capacity,length) in dp:
        return dp[(capacity,length)]
    if capacity==0 or length==0:
        return 0
    if weight[length-1] > capacity:
        ans=knap(capacity,length-1)
        dp[(capacity,length)]=ans
        return ans
    else:
        ans=max(value[length-1]+knap(capacity-weight[length-1],length-1),
                   knap(capacity,length-1))
        dp[(capacity,length)]=ans
        return ans

##solution second
def knap_bottom(capacity,length):
    table = list()
    for i in xrange(capacity+1):
        table.append([0]*(length+1))
    for i in xrange(1,capacity+1):
        for j in xrange(1,length+1):
            if weight[j-1] <= i:
                table[i][j]=max(value[j-1]+table[i-weight[j-1]][j-1],table[i][j-1])
            else:
                table[i][j]=table[i][j-1]
    for i in table:
        print i
    return table[-1][-1]
value=[3,4,5,6]
weight=[2,3,4,5]
capacity= 5
print knap_bottom(capacity,len(value))
#print knap(capacity,len(value))


