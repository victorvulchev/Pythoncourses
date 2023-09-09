a = float(input())
b = float(input())
c = float(input())

if a >= b and b >= c:
    print(c, b, a)
elif b >= c and c >= a:
    print(a, c, b)
elif c >= b and b >= a:
    print(a, b, c)
elif c >= a and a >= b:
    print(b, a, c)
elif a >= c and c>= b:
    print(b, c, a)
else:
    print(c, a, b)