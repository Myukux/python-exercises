number_list = []

for number in range(1000, 3001):
    is_fully_even = True
    number_string = str(number)

    for digit in number_string:
        if int(digit) % 2 != 0:
            is_fully_even = False

    if is_fully_even:
        number_list.append(number_string)

number_list_as_str = ", ".join(number_list)
print(number_list_as_str)
