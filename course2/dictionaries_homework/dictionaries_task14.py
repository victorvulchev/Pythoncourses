yearly_earnings = {"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0}
sorted_dict = sorted(yearly_earnings.items(), key=lambda item:item[1], reverse=True)
print (sorted_dict)

for i,j in sorted_dict:
    hashtag = j // 50
    bricks = ""
    for k in range(hashtag):
        bricks += "#"
    bricks += " "
    print(f"{i}:{bricks}{j}")

