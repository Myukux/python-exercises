words = "mama ma kota mama ala ala piesa kota"
words = words.split()

result = sorted(words)

result_list = []

for word in result:
    if word not in result_list:
        result_list.append(word)

result_words = " ".join(result_list)
print(result_words)
