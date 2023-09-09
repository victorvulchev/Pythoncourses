numb = int(input())

if numb < 10:
    for i in range(1, numb):
        print(i, end="-")
    if numb > 0:
        print(numb)
else:
    for i in range(1, numb + 1):
        if i < 10:
            print(i, end="-")
        else:
            bigger_number = str(i)
            to_print = bigger_number[:1] + "-" + bigger_number[1:]
            if i != numb:
                print(to_print, end="-")
            else:
                print(to_print)

