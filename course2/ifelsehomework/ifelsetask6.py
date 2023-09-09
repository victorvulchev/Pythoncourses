a = int(input())
b = int(input())
c = int(input())

if a + b == 0:
    print(f"the sum of {a} and {b} is 0")
elif a + c == 0:
    print(f"the sum of {a} and {c} is 0")
elif b + c == 0:
    print(f"the sum of {b} and {c} is 0")
else:
    print("No sums equal 0")