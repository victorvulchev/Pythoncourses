word_1 = input("First Word:")
word_2 = input("Second Word:")
counter = 0

if len(word_1) == len(word_2):
    for i in range(len(word_1)):
        if word_1[i] in word_2:
            counter += 1
    if counter == len(word_1):
        print("Words are annagrams")
else:
    print("Not Annagrams")

