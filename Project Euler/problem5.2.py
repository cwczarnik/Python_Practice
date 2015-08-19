import time
start_time = time.time()

def ProjectEulerFive (m = 20):

    a = m
    start = 11

    b = start
    while b < m:
        if (a % b)!= 0:
           a += m
           b = start
           continue
        else:
            b += 1
    return a

print ProjectEulerFive()
print "took " + str(time.time() - start_time ) + " seconds"
