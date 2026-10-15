def prime_sieve(limit):
    is_prime = [True] * (limit + 1)

    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []

    for number in range(2, limit + 1):
        if is_prime[number]:
            primes.append(number)

    return primes


primes = prime_sieve(1000)

print("Prime numbers up to 1000:")
print(primes)

print("Highest prime number generated:", primes[-1])
