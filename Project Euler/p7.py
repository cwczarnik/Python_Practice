import numpy
from numpy import *
import time
start_time = time.time()
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
    
    print p-1
    print "time " + str(time.time() - start_time ) + " seconds"
nthprime(10001) 
