student_scores = {
 "Susan": [67, 84, 75, 63],
 "Mike": [87, 98, 64, 71],
 "Jim": [90, 58, 73, 86]
}
new_dict = {}

for i in student_scores:
    points = 0
    for j in student_scores[i]:
        points += j
    average = points / len(student_scores[i])
    new_dict[i] = average

sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1],reverse=True))

print(next(iter(sorted_dict.keys())))
