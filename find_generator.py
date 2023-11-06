from sympy import primefactors
import helpers

def find_generator(p):
    for g in range(2, p-1):
        if all(helpers.mod_exp(g, (p-1)//f, p) != 1 for f in primefactors(p-1)):
            return g
