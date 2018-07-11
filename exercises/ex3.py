n = int(input("podaj liczbe: "))
a = {}
for i in range(1, n + 1):
    j = i ** 2
    a[i] = j
print(a)
