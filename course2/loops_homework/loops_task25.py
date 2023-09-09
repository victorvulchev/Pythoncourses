n = int(input("N:"))
x = int(input("X:"))
one = 1
if n == 0 or x == 0:
    print("Грешка, не може да се дели на нула.")
else:
    for i in range(1, n+1):
        i_fact = 1
        for j in range(1, i+1):
            i_fact *= j
        one += i_fact / x**i
print(one)
