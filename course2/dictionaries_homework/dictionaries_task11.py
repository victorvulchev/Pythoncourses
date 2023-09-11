bingo_card = {}
bingo_card["B"] = []
bingo_card["I"] = []
bingo_card["N"] = []
bingo_card["G"] = []
bingo_card["O"] = []
import random
for i in range(5):
    numb = random.randint(1, 15)
    bingo_card["B"].append(numb)
    numb = random.randint(16, 30)
    bingo_card["I"].append(numb)
    numb = random.randint(31, 45)
    bingo_card["N"].append(numb)
    numb = random.randint(46, 60)
    bingo_card["G"].append(numb)
    numb = random.randint(61, 75)
    bingo_card["O"].append(numb)

for i in bingo_card.keys():
    print(i, end="  ")
print(" ")

for i in range(len(bingo_card["B"])):
    for j in bingo_card.keys():
        print(bingo_card[j][i], end= " ")
    print(" ")