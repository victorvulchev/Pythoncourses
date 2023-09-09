the_list = [1,2,3]

for i in range(len(the_list)+1):
    for j in range(i + 1, len(the_list) + 1):
        newer_list = []
        new_list = the_list[i:j]
        newer_list.append(new_list)
        print(newer_list)
