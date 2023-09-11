one_point = "AEILNORSTU"
two_points ="DG"
three_points = "BCMP"
four_points = "FHVWY"
five_points = "K"
eight_points = "JX"
ten_points = "QZ"

scrabble = {}

for i in range(len(one_point)):
    scrabble[one_point[i]] = 1
for i in range(len(two_points)):
    scrabble[two_points[i]] = 2
for i in range(len(three_points)):
    scrabble[three_points[i]] = 3
for i in range(len(four_points)):
    scrabble[four_points[i]] = 4
for i in range(len(five_points)):
    scrabble[five_points[i]] = 5
for i in range(len(eight_points)):
    scrabble[eight_points[i]] = 8
for i in range(len(ten_points)):
    scrabble[ten_points[i]] = 10

word = input()
points = 0

for i in range(len(word)):
    points += scrabble[word[i]]

print(points)

