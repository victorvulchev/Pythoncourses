points = int(input())

if points >= 1 and points <= 3:
    print(points * 10)
elif points >= 4 and points <= 6:
    print(points * 100)
elif points >= 7 and points <= 9:
    print(points * 1000)
else:
    print("error")