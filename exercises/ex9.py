a = input("ile chcesz podac zdan?:")
a = int(a)
c = []
for i in range(1, a + 1):
    b = input("podaj zdanie: ")
    b = b.upper()
    c.append(b)
for j in c:
    print(j)

