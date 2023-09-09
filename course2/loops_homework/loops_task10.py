numb = int(input())
final_number = 0
index = 1
temp_numb = 0
for i in range(1, numb + 1, 1):
    for j in range(1, i):
        temp_numb = index * (index + j)
        if j != i:
            continue
        else:
            index += j
    final_number += temp_numb
    temp_numb = 0
print(final_number)        
    