numb = input()
numbs = []

while numb != "":
    numbs.append(int(numb))
    numb = input()

new_numbs = []
current_pos = 0
for i in range(len(numbs)):
    if numbs[i] < 0:
        if current_pos < i:
            current_pos += 1
        new_numbs.insert(current_pos, numbs[i])
    else:
        new_numbs.append(numbs[i])
zero_counter = 0
for i in new_numbs:
    if i == 0:
        new_numbs.remove(i)
        zero_counter += 1
for i in range(zero_counter):
    for j in range(len(new_numbs)):
        if new_numbs[j] > 0:
            new_numbs.insert(j, 0)
            break
print(new_numbs)
