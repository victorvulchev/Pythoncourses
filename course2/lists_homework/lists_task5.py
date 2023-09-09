import random
winning_numbs = []
while len(winning_numbs) != 6:
    numb = random.randint(1, 49)
    if numb not in winning_numbs:
        winning_numbs.append(numb)
winning_numbs.sort()
print(winning_numbs)
