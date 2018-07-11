numbers = input("Podaj Liczby, odzielajac je przecinkiem: ")
a = numbers.split(",")
result = []
for i in a:
    i = int(i)
    k = 1
    for j in range(1, i + 1):
        k = k * j
    result.append (str(k))

result = ",".join(result)
print(result)
