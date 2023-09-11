list = ["HaPPy", "mOOdy", "yummy", "mayBE"]
dict = {}

for i in list:
    counter = 0
    for j in i:
        if j.isupper():
            counter += 1
    if counter not in dict:
        dict[counter] = [i]
    else:
        dict[counter].append(i)
for i, j in dict.items():
    print(f"{i}:{j}")
