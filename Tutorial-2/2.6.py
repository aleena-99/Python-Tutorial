def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_primes_composites(lst):
    primes = [n for n in lst if is_prime(n)]
    composites = [n for n in lst if n > 1 and not is_prime(n)]
    return primes, composites

print(separate_primes_composites([2, 4, 5, 9, 11, 15, 17]))
