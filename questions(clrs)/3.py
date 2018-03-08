for _ in range(input()):
    n,q=map(int,raw_input().split())
    array=list(map(int,raw_input().split()))
    ans_array=[0]
    array.sort()
    l,size=len(array),array[-1]+(len(array))
    for i in range(1,size):
        index=0
        for j in range(l):
            if(array[j]>=i):
                index=j-1
                break
        if(index==-1):
            ans_array.append(l)
            continue
        elif(i>array[-1]):
            ans_array.append(0)
            continue
        start,end,ans,factor=0,index,0,0
        while(start<end):
            if(array[end]+1+factor==i):
                ans+=1
                start+=1
                end-=1
            elif(array[end]+1+factor<i):
                start+=1
                factor+=1
        ans+=l-(index+1)
        ans_array.append(ans)
    for i in range(q):
        num=input()
        if(num>=size):
            print 0
        else:
            print ans_array[num]
            
    


    
        
