##longest common substring
def sub_string(s1,s2):
    l1,l2=len(s1),len(s2)
    temp,store=[0]*(l1+1),list()
    for i in range(l2+1):
        store.append(list(temp))
    for i in range(1,l2+1):
        for j in range(1,l1+1):
            if(s1[j-1]==s2[i-1]):
                store[i][j]=1+store[i-1][j-1]
            else:
                store[i][j]=max(store[i-1][j],store[i][j-1])
    ans=''
    i,j=l2,l1
    while(store[i][j]):
        if(s1[j-1]==s2[i-1]):
            i,j=i-1,j-1
            ans+=s1[j]
        else:
            if(store[i-1][j]>store[i][j-1]):
                i-=1
            else:
                j-=1
    return ans[-1::-1]

