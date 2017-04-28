##Sieve of Atkin fastest prime list
def add_prime(limit):
    prime= [False for i in range(limit)]
    x=1
    while(x*x<limit):
        y=1
        while(y*y<limit):
            n = (4*x*x)+(y*y)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                prime[n]=True
            n = (3*x*x)+(y*y)
            if (n <= limit and n % 12 == 7):
                prime[n]=True
            n = (3*x*x)-(y*y)
            if (x > y and n <= limit and n % 12 == 11):
                prime[n]=True
            y+=1
        x+=1
    i=5
    while(i*i<limit):
        if(prime[i]):
            j=i*i
            while(j<limit):
                prime[j]=False
                j+=(i*i)
        i+=1

    '''print using sieve'''
    for i in range(5,limit):
        if(prime[i]):
            print(i,end=' ')
