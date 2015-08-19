def prime_list(limit):
        if limit < 2:
                return []
        sieve_size = limit / 2
        sieve = [True] * sieve_size
 
        for i in range(0, int(limit ** 0.5) / 2):
                if not sieve[i]:
                        continue
                for j in range((i * (i + 3) * 2) + 3, sieve_size, (i * 2) + 3):
                        sieve[j] = False
 
        primes = [2]
        primes.extend([(i * 2) + 3 for i in range(0, sieve_size) if sieve[i]])
 
        return primes
 
print reduce(lambda x,y: x+y, prime_list(2000000))
