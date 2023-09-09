rows = int(input())
cols = int(input())

for row in range(1, rows + 1):
    for col in range(1, cols + 1):
        if col % 2 == 1:
            print((col - 1) * rows + row, end=" ")
        else:
            print(col * rows - row + 1, end=" ")
    print()
