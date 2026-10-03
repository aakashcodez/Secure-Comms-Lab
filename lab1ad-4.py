import random

def miller_rabin(n, k=20):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    # Write n - 1 as 2^s * d
    s = 0
    d = n - 1

    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform k testing rounds
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


numbers = [
    5,
    7919,
    858599509,
    982451653,
    982451652
]

for number in numbers:
    if miller_rabin(number):
        print(number, "is probably prime")
    else:
        print(number, "is composite")
