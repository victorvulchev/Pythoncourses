a = int(input())
b = int(input())
result = a * b
last_numb = result % 10
if not last_numb % 2 == 0:
    print(f"{result}, {last_numb} not even")
else:
    print(f"{result}, {last_numb} even")

