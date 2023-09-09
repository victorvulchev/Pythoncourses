x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 <= x2 and y1 <= y2) or (x1 <= y2 and y1 <= x2):
    print("can fit")
else:
    print("can't fit")