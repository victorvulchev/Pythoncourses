word = input("Enter a word:")
og_list = []
list_to_print=[]

while word != "":
    og_list.append(word)
    if word not in list_to_print:
        list_to_print.append(word)
    word = input("Enter a word:")
for i in list_to_print:
    print(i)