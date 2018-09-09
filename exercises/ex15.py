digit = input("Podaj cyfre")
a = 0

for i in range(1, 5):
    number = int(digit * i)
    a += number

print(a)
