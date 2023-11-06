from babystepgiantstep import babystepgiantstep
import helpers
import math
import time


def prime_factors(n): 
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    return factors

def factor_powers(n):
    factors = prime_factors(n)
    result = {}
    for factor in factors:
        if factor in result:
            result[factor] += 1
        else:
            result[factor] = 1
    return result

def chinese_remainder_theorem(moduli, remainders):
    product = 1
    for modulus in moduli:
        product *= modulus
    N = product
    x = 0
    for mi, ri in zip(moduli, remainders):
        Ni = N // mi
        xi = helpers.modular_inverse(Ni, mi)
        x += ri * xi * Ni
    return x % N

def pohlig_hellman(n, alpha, beta):
    factorization = factor_powers(n)
    moduli = []
    remainders = []
    for p, e in factorization.items():
        pe = p ** e
        n_i = n // pe
        alpha_i = pow(alpha, n_i, n)
        beta_i = pow(beta, n_i, n)
        x_i = babystepgiantstep(pe, alpha_i, beta_i)
        moduli.append(pe)
        remainders.append(x_i)
    return chinese_remainder_theorem(moduli, remainders)

if __name__ == "__main__":
    n = 17**5
    g = 5
    h = 41
    t1 = time.time()
    x = pohlig_hellman(n, g, h)
    t2 = time.time()
    print(f"p: {n}  g: {g}  h: {h}")
    print(f"Computed x: {x}")
    print("Successfully found the discrete logarithm!")
    print(f"Time elapsed = {t2-t1}")
