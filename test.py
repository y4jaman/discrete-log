x = 737135
n = 1419857
g = 5
h = 1
for i in range(x):
    h = (h * g) % n
print(h)