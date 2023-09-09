a = 0
b = 1
result = 1
while result < 50:
    
    if a == 0:
        print(a, end=", ")
        print(b, end=", ")

    print(result, end=", ")
    a = b
    b = result
    result = a + b


