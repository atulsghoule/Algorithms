##Sieve of Atkin
prime= [False]*(limit+1)
def add_prime(limit):
    prime[2]=prime[3]=True
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

##Sieve of Eratosthenes
import math
sieve=[True]*(limit+1)
def add_prime2(limit):
    for i in range(2,int(math.sqrt(limit))+1):
        if(sieve[i]==True):
            for j in range(i*2,limit+1,i):
                sieve[j]=False

        
