def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    return [i for i in range(2, limit + 1) if is_prime[i]]


for limit in [100, 1000, 5000, 10000]:
    primes = prime_sieve(limit)
    print(f"Up to {limit}: {primes[-1]}")
