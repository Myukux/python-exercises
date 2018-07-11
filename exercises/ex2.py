numbers = input("Podaj Liczby, odzielajac je przecinkiem: ")
a = numbers.split(",")
print(a)
for i in a:
    for j in i:
        i = int(i)
        i = i * (j - 1)
     print(i)
