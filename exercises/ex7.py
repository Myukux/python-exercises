a = input("podaj dwa numery odzielajac je przecinkami: ")
a = a.split(",")
c = []
b = int(a[0])
d = int(a[1])
for i in range(0, b):
    c.append([])
    for j in range(0, d):
        r = i * j
        c[i].append(r)

print(c)
