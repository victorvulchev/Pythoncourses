a = float(input())
b = float(input())
c = float(input())

import math

discriminant = b**2 - (4 * a * c)

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant))/ (2 * a)
    root2 = (-b - math.sqrt(discriminant))/ (2 * a)
    print(root1)
    print(root2)
else:
    print("No roots")
