import random
from sympy import primefactors
import helpers
import time
import math

def generate_relations(p, g, factor_base, num_relations):
    relations = []
    x_values = []

    while len(relations) < num_relations:
        x = random.randint(1, p - 1)
        gx = helpers.mod_exp(g, x, p)
        factors = primefactors(gx)
        if all(f in factor_base for f in factors):
            relations.append(factors)
            x_values.append(x)

    return relations, x_values

def build_matrix(p, factor_base, relations):
    matrix = []

    for relation in relations:
        row = [0] * len(factor_base)
        for f in relation:
            row[factor_base.index(f)] = (row[factor_base.index(f)] + 1) % 2
        matrix.append(row)

    return matrix

def gaussian_elimination(matrix):
    row, col = 0, 0

    while row < len(matrix) and col < len(matrix[0]):
        if matrix[row][col] == 0:
            for r in range(row + 1, len(matrix)):
                if matrix[r][col] == 1:
                    matrix[row], matrix[r] = matrix[r], matrix[row]
                    break
            else:
                col += 1
                continue

        for r in range(row + 1, len(matrix)):
            if matrix[r][col] == 1:
                matrix[r] = [(matrix[r][c] - matrix[row][c]) % 2 for c in range(len(matrix[0]))]

        row += 1
        col += 1

    return matrix

def find_log(p, g, h, factor_base, matrix, x_values):
    for row in matrix:
        if sum(row) == 1:
            i = row.index(1)
            x = x_values[matrix.index(row)]
            log_g_h = x * factor_base[i] % (p - 1)
            if helpers.mod_exp(g, log_g_h, p) == h:
                return log_g_h

def index_calculus(p, g, h, bound, num_relations):
    factor_base = [-1] + primefactors(p-1)[:bound]
    relations, x_values = generate_relations(p, g, factor_base, num_relations)
    matrix = build_matrix(p, factor_base, relations)
    reduced_matrix = gaussian_elimination(matrix)
    result = find_log(p, g, h, factor_base, reduced_matrix, x_values)

    return result

if __name__ == '__main__':
    p = 49
    g = 2
    h = 41
    bound = 20
    num_relations = 100
    log_g_h = None
    t1 = time.time()
    while(True):
        log_g_h = index_calculus(p, g, h, bound, num_relations)
        if(log_g_h != None):
            break
        print("FAIL")
    t2 = time.time()
    print(f"p: {p}  g: {g}  h: {h}")
    print(f"Computed x: {log_g_h}")
    print("Successfully found the discrete logarithm!")
    print(f"Time elapsed = {t2-t1}")

