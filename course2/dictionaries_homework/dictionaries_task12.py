word = input("Enter a word:")
new_word = word.lower()
dict = {}
for i in range(len(new_word)):
    if new_word[i] not in dict:
        dict[new_word[i]] = 1
    else:
        dict[new_word[i]] += 1
for i, j in dict.items():
    print(f"{i}:{j}")
