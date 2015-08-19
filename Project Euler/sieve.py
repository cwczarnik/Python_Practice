import numpy
from numpy import *
import time
start_time = time.time()
def sieve_eratosthenes(n):
    """
    Returns a list of prime numbers less than n
    """
    if n < 2:
        return []
  
    # Marks an index as a prime (True) or non-prime (False)
    sieve = [True] * n
    p = 3
    # All numbers less than p^2 are marked, terminate if p^2 < n
    while p**2 < n:
        if sieve[p]:
            i = p**2
            # Check start at p^2, multiple of p
            for j in xrange(i, n, 2*p):
                sieve[j] = False
        p += 2
  
    primes = [2]
    # All non-even Trues after 3 are prime
    for i in xrange(3, len(sieve), 2):
        if sieve[i]: primes.append(i)
   
    return primes


print(max(sieve_eratosthenes(12)))
print "time " + str(time.time() - start_time ) + " seconds"
