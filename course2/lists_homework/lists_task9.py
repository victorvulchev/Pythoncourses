rows = int(input("Rows:"))
colums = int(input("Colums:"))

for i in range(1,rows + 1):
    print(i, end=" ")
    numb = i
    for j in range(1, colums):
        numb += rows
        print(numb, end=" ")
    print(" ")
#don't know how to do the other
# +4 then -1
print("-" * 10)

for i in range(1, rows + 1):
    for j in range(1, colums + 1):
        if j % 2 == 1:
            print((j - 1) * rows + i, end=" ")
        else:
            print(j * rows - i + 1, end=" ")
    print()


