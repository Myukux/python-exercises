a = input("podaj slowa, oddzielajac je przecinkami: ")
a = a.split(",")
a = sorted(a)
a = ",".join(a)
print(a)
