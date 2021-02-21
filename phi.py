from math import gcd

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def find_d(phi_n, c, d=1):
    while (c*d) % phi_n != 1:
        d += 1
    return d

def ggt(a, b):
    if b==0:
        return a
    else:
        return ggt(b, a%b)

n = int(input("Gib mir das n: "))
n = phi(n)
print("Phi von n: {}".format(n))
c = int(input("Hast du c oder d: "))
if ggt(n,c) != 1:
    print("ggT ist nicht 1. Abbruch.")
    exit(1)
print("Ergebnis: {}".format(find_d(n,c)))
