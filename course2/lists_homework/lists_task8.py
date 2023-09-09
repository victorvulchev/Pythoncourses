the_list = [3, 2, 3, 4, 2, 2, 4]
increacing_list = []
current_list = [the_list[0]]

for i in range(1, len(the_list)):
    if the_list[i - 1] < the_list[i]:
        current_list.append(the_list[i])
    else:
        current_list = [the_list[i]]
    if len(current_list) > len(increacing_list):
        increacing_list = current_list[:]
print(increacing_list)