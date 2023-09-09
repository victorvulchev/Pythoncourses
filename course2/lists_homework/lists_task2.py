numb = int(input("Enter more than four number. When done, type 0:"))
numbs = []

while numb != 0:
    numbs.append(numb)
    numb = int(input("Enter more than four number. When done, type 0:"))

if len(numbs) <= 4:
    print("You have entered 4 or less numbers")
else:
    copy = numbs[:]

    for i in range(2):
        smallest_numb = min(copy)
        biggest_numb = max(copy)
        copy.remove(smallest_numb)
        copy.remove(biggest_numb)
    print(copy)
    print(numbs)
    

    
