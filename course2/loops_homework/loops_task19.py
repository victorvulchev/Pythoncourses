word = input()
space = " "

if space in str(word):
    new_text = str(word).split(" ")
    for i in new_text:
        reversed_word = ""
        if len(i) % 2 != 0:
            for j in range(len(i) - 1, -1, -1):
                reversed_word += i[j]
            if i == new_text[len(new_text) - 1]:
                print(reversed_word)
            else:
                print(reversed_word, end=" ")
        else:
            if i == new_text[len(new_text) - 1]:
                print(i)
            else:
                print(i, end= " ")
else:
    if len(word) % 2 != 0:
        reversed_word = ""
        for i in range(len(word) - 1, -1, -1):
            reversed_word += word[i]
        print(reversed_word)
    else:
        print(word)
