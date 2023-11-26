import time


def trial_division(n):
    start_time = time.time()

    divisors = []
    iter_count = 0

    while n % 2 == 0:
        divisors.append(2)
        n //= 2
        iter_count += 1
    f = 3
    while f * f <= n:
        if n % f == 0:
            divisors.append(f)
            n //= f
        else:
            f += 2
        iter_count += 1
    if n != 1:
        divisors.append(n)

    end_time = time.time()

    elapsed_time = end_time - start_time

    return (divisors, elapsed_time, iter_count)
