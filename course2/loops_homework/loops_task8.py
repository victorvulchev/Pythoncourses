stars = "*****"
line = 1
while line != 7:
    if line == 1:
        print(f" {stars[1:-1]} ")
        line += 1
    elif line == 4:
        print(stars)
        line += 1
    else:
        print("*   *")
        line += 1

    