import math
import time
import helpers

def shanks(n,alpha,beta):
    result = None
    m = math.ceil(math.sqrt(n))
    j_table = [None for i in range(m)]
    alpha_power_mj = 1
    alpha_power_m = alpha**m
    for j in range(m):
        temp = (alpha_power_mj) % n
        j_table[j] =(j, temp)
        alpha_power_mj *= alpha_power_m

    inverse_alpha = helpers.modular_inverse(alpha, n)
    j_table = helpers.merge_sort(j_table)

    temp = beta
    i_table = [None for i in range(m)]
    for i in range(m):  
        i_table[i]= (i,temp)
        temp = (temp*inverse_alpha) % n

    i_table = helpers.merge_sort(i_table)

    for item in j_table:
        for element in i_table:
            if element[1] > item[1]:
                break
            if item[1] == element[1]:
                result = (m*item[0] + element[0]) % n
                return result
    return result

if __name__ == "__main__":
    n = 17**5
    g = 5
    h = 41
    t1 = time.time()
    x = shanks(n,g,h)
    t2 = time.time()
    print(f"p: {n}  g: {g}  h: {h}")
    print(f"Computed x: {x}")
    print("Successfully found the discrete logarithm!")
    print(f"Time elapsed = {t2-t1}")