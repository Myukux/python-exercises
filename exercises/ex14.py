input_string = "abc def abc !123m543pRFD"
lower = 0
upper = 0

for a in input_string:
    if a.islower():
        lower += 1
    if a.isupper():
        upper += 1
print(upper)
print(lower)

