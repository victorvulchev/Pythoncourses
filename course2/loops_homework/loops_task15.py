numb = int(input())
if numb == 1 or numb == 2:
    print("This is a prime number")
else:
    for i in range(2, numb + 1):
        if i == numb:
            print("This is a prime number")
        elif numb % i == 0:
            print("This is NOT a prime number")
            break