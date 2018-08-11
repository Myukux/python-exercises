

# a = input("Podaj słowa odzielając je spacją: ")
# a = a.split(" ")
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# a = sorted(a)
# a = " ".join(a)
# print(a)

a = input("Podaj słowa odzielając je spacją: ")
a = a.split(" ")
c = []
for i in a:
    does_exist_in_list = False
    for j in c:
        if i == j:
            does_exist_in_list = True
            break
    if not does_exist_in_list:
        c.append(i)
c = sorted(c)
c = " ".join(c)
print(c)
