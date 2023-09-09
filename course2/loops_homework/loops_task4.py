word = input()
buff = ""
for i in range(len(word) - 1, -1, -1):
    buff += word[i]
print(buff)