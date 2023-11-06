import time
import math
import helpers

def babystepgiantstep(n,alpha,beta):
    result = None
    table = []
    m = math.ceil(math.sqrt(n))
    for j in range(m):
        temp = (alpha**j) % n
        table.append((j, temp))
    inverse_alpha = helpers.modular_inverse(alpha, n)

    temp = inverse_alpha
    for i in range(m-1):
        temp = (temp*inverse_alpha) % n

    y = beta
    for i in range(m):
        for j in range(m):
            if (y == table[j][1]):
                result = (i*m + table[j][0]) % n
                return result
        y = (y*temp) % n
    return result

if __name__ == "__main__":
    n = 17**5
    g = 5
    h = 41
    t1 = time.time()
    x = babystepgiantstep(n,g,h)
    t2 = time.time()
    print(f"p: {n}  g: {g}  h: {h}")
    print(f"Computed x: {x}")
    print("Successfully found the discrete logarithm!")
    print(f"Time elapsed = {t2-t1}")