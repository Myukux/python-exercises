words = "mama ma kota mama ala ala piesa kota"
words = words.split()

result = sorted(words)

result_list = []

for word in result:
    if word not in result_list:
        result_list.append(word)

print(result_list)
