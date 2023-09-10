dictionary = {"hello" : "здравей",
              "food" : "храна",
              "water" : "вода"}

word = input("Search word:")
if word in dictionary.keys():
    print(dictionary[word])
else:
    no_word = []
    print(no_word)