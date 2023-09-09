a = int(input())
b = int(input())
operation = input()

if operation == "+":
    result = a + b
    if result % 2 == 0:
        print(f"{a} {operation} {b} = {result} - even")
    else:
        print(f"{a} {operation} {b} = {result} - odd")
elif operation == "-":
    result = a - b
    if result % 2 == 0:
        print(f"{a} {operation} {b} = {result} - even")
    else:
        print(f"{a} {operation} {b} = {result} - odd")
elif operation == "*":
    result = a * b
    if result % 2 == 0:
        print(f"{a} {operation} {b} = {result} - even")
    else:
        print(f"{a} {operation} {b} = {result} - odd")
elif operation == "/":
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        result = a / b
        print(f"{a} / {b} = {result:.2f}")
else:
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        result = a % b
        print(f"{a} % {b} = {result}")