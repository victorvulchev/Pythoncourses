n = int(input("N:"))
k = int(input("K:"))
p = n - k
n_fact = 1
k_fact = 1
p_fact = 1

if k >= n:
    print("K трябва да е по-малко от N") 
elif k == 0 or n == 0:
    print("Невалиден вход")
else:
    for i in range(1,n + 1):
        n_fact *= i
    for i in range(1,k + 1):
        k_fact *= i
    for i in range(1,p + 1):
        p_fact *= i
    result = n_fact * k_fact // p_fact
    print(result)
