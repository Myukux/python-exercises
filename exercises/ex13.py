input_string = "abc def abc !123m543p?"

letter_count = 0
number_count = 0

for letter in input_string:
    if letter.isdigit():
        number_count += 1
    if letter.isalpha():
        letter_count += 1

print(letter_count)
print(number_count)

