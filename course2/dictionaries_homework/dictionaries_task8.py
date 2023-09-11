word = input()
counter = 0
dict = {}

for i in range(0, len(word)):
    if word[i] not in dict:
        counter += 1
        dict[word[i]] = word[i]
print(f"Unique symbols:{counter}")
for i, j in dict.items():
    print(f"{i}:{j}")