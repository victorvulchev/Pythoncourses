numb = int(input("Enter numbers:"))
numbs = []

while numb != 0:
    numbs.append(numb)
    numb = int(input("Enter numbers:"))

numbs.sort()
for i in numbs:
    print(i)
