## coin change problem
##solution first
dp={}
def count(coins,money,size):
    if (money,size) in dp:
        return dp[(money,size)]
    if money==0:
        return 1
    if money<0:
        return 0
    if size<=0 and money>=1:
        return 0
    ans=count(coins,money,size-1)+count(coins,money-coins[size-1],size)
    dp[(money,size)]=ans
    return ans



##solution second
def count_bottom(coins,money):
    table = list()
    
    for i in xrange(money+1):
        table.append([0]*len(coins))

    for i in xrange(len(coins)):
        table[0][i]=1
        
    for i in xrange(1,money+1):
        for j in xrange(len(coins)):
            x,y=0,0
            ## including that coin (money-coins[size-1]),size-1
            if i-coins[j]>=0:
                x=table[i-coins[j]][j]
            ##excuding that coin (money,size-1)
            if j>=1:
                y=table[i][j-1]
            table[i][j]=x+y
    return table[-1][-1]

            
##solution third
def count_best(coins,money):
    table = [0]*(money+1)
    table[0]=1
    for i in xrange(len(coins)):
        for j in xrange(coins[i],money+1):
            table[j]+=table[j-coins[i]]
    return table[-1]

money=5
coins = [1,2,3,4,5]
print count(coins,money,len(coins))
print dp
print count_bottom(coins,money)
print count_best(coins,money)







        
    
