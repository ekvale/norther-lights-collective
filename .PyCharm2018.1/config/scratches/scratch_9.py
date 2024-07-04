import math
import time

def primeFactors(n):
    print(time.time())
    while n % 2 == 0:
        print("Dividing by two: ")
        n = n/2
        print(n)

    for num in range(3, int(math.sqrt(n)) + 1, 2):
        while n % num == 0:
            print("Prime Factor: ", num)
            n = n/num

    if n > 2:
        print("Prime: ", n, "\n", time.time())


primeFactors(160000020800000387)


