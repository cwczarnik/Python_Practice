import numpy
from numpy import *
import time
start_time = time.time()

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
#104743

#check primality of the number
prime =[]
 p = 2
for i in xrange(2,N):
    if p%i ==0:
        
        
   

def nthprime(N):
    A =[x**(1/2) for x in xrange(2,N)]
    p = 2
    while p < N:
        for i in A:
          if A[i] is True:
            for j in A:
                j = i**2+i
                A.append(j)
                A[j] = False
            
          p+=1
          
        return A
          
    
print nthprime(25)
   
    
#iterate through a series of numbers

print is_prime(3)
 print "time " + str(time.time() - start_time ) + " seconds"
