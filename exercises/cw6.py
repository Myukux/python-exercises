from math import sqrt

d = input("Podaj liczby odzielajac je przecinkami: ")
d = d.split(",")
c = 50
h = 30
k = []
for i in d:
    i = int(i)
    q = sqrt((2 * c * i) / h)
    k.append(str(q))
k=", ".join(k)
print(k)

