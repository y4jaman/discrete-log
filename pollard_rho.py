import helpers
import time

def pollard_rho(n,alpha,beta):  

    def f(x):
        if x % 3 == 0:  
            return (x*x) % n
        if x % 3 == 1:
            return (alpha*x) % n
        if x % 3 == 2:
            return (beta*x) % n
    
    def g(x,k):
        if x % 3 == 0:
            return (2*k) % (n-1)
        if x % 3 == 1:
            return (k + 1) % (n-1)
        if x % 3 == 2:
            return k

    def h(x,k):
        if x % 3 == 0:
            return (2*k) % (n-1)
        if x % 3 == 1:
            return k
        if x % 3 == 2:
            return (k + 1) % (n-1)
            
    a = [None for i in range(n*2)]
    b = [None for i in range(n*2)]
    x = [None for i in range(n*2)]

    a[0] = 0
    b[0] = 0
    x[0] = 1

    i = 1

    while(True):
        x[i] = f(x[i-1])
        a[i] = g(x[i-1], a[i-1])
        b[i] = h(x[i-1], b[i-1])

        x[2*i] = f(f(x[2*i-2]))
        a[2*i] = g(f(x[2*i-2]), g(x[2*i-2], a[2*i-2]))
        b[2*i] = h(f(x[2*i-2]), h(x[2*i-2], b[2*i-2]))

        if x[i] == x[2*i]:
            r = b[i] - b[2*i]
            if r == 0:
                return -1
            result = ((helpers.modular_inverse(r,n))*(a[2*i] - a[i])) % (n)
            return result
        else:
            i = i+1

if __name__ == "__main__":
    n = 1019
    g = 2
    h = 5
    t1 = time.time()
    print(pollard_rho(n,g,h))
    t2 = time.time()
    print(f"p: {n}  g: {g}  h: {h}")
    print(f"Computed x: {n}")
    print("Successfully found the discrete logarithm!")
    print(f"Time elapsed = {t2-t1}")