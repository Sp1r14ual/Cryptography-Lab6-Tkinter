import time


def sieve(n):
    start_time = time.time()

    arr = set(range(2, n+1))
    sieve = set()
    iter_count = 0
    while arr:
        prime = min(arr)
        sieve.add(prime)
        arr -= set(range(prime, n+1, prime))
        iter_count += 1

    end_time = time.time()

    elapsed_time = end_time - start_time

    return (sieve, elapsed_time, iter_count)
