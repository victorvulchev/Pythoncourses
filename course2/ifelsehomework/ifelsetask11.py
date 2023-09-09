a = float(input())
b = float(input())
c = float(input())
import math
m_a = math.sqrt((2 * c**2) + (2 * b**2) - a**2) / 2
m_b = math.sqrt((2 * c**2) + (2 * a**2) - b**2) / 2
m_c = math.sqrt((2 * a**2) + (2 * b**2) - c**2) / 2

print(m_a)
print(m_b)
print(m_c)