from math import gcd

x = int(input("Gib mir die Nachricht: "))
c = int(input("Gib mir den Schlüssel: "))
n = int(input("Gib mir das n: "))

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

phi_n = phi(n)
new_c = c % phi_n
if new_c < c:
    print("Ich habe deinen Schlüssel vereinfacht zu: {}".format(new_c))
erg = (x ** new_c) % n
print("Ergebnis: {}".format(erg))
