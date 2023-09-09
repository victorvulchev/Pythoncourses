numbs = input()
list_numbs = numbs.split(",")
even = 0
odd = 0
for i in range(0, len(list_numbs), 1):
    if int(list_numbs[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Number of even numbers:{even}")
print(f"Number of odd numbers:{odd}")