'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import numpy
from numpy import *

m = 1000
#find primes
#142913828922

def nthprime(num):
     
    cnt = 1
    p = 2
    primes = [2]
    
    while cnt < num:
        
        for i in primes:
            if p % i == 0:
                break
        else:
            primes.append(p)
            cnt += 1
            
        p +=1
    
    return p-1

#sum primes
for i in xrange(0,m):
    x = sum(nthprime(i))

else:
    print x
