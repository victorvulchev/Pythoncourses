line = 1
stars_1 = "*       *"
while line != 7:
    if line == 3:
        print("* *   * *")
    elif line == 4:
        print("*   *   *")
    else:
        print(stars_1)
    line += 1

line = 1
stars_1 = "*   *"
stars_2 ="****"
while line != 8:
    if line == 1 or line == 7:
        print(stars_2)
    else:
        print(stars_1)
    line += 1