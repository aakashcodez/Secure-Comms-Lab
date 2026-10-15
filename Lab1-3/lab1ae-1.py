def linear_congruential(a, seed, c, m, count):
    x = seed

    for i in range(count):
        x = (a * x + c) % m
        print(x)


a = 2175143
seed = 3553
c = 10653
m = 1000000

linear_congruential(a, seed, c, m, 10)
