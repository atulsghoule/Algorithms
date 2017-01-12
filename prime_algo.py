##Sieve of Atkin fastest prime list
import math as m
def add_prime(limit):
    '''2 and 3 are prime which is not included'''

    ''' Initialise the sieve array with false values'''
    prime= [False for i in range(limit)]

    '''Mark prime[n] is true if one of the following is true:
     a) n = (4*x*x)+(y*y) has odd number of solutions, i.e., there exist
        odd number of distinct pairs (x, y) that satisfy the equation and
        n % 12 = 1 or n % 12 = 5.
     b) n = (3*x*x)+(y*y) has odd number of solutions and n % 12 = 7
     c) n = (3*x*x)-(y*y) has odd number of solutions, x > y and n % 12 = 11 '''
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

    '''Mark all multiples of squares as non-prime'''
    i=5
    while(i*i<limit):
        if(prime[i]):
            j=i*i
            while(j<limit):
                prime[j]=False
                j+=1
        i+=1

    '''print using sieve'''
    for i in range(5,limit):
        if(prime[i]):
            print(i,end=' ')
