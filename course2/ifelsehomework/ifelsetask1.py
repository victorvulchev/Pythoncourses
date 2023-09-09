a = int(input())
b = int(input())
temp_a = a
print(a, b)
if a > b:
    a = b
    b = temp_a
print(a, b)