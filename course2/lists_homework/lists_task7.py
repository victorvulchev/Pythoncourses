the_list = [2, 1, 1, 2, 3, 3, 2, 2, 2, 1]
longest_siquence = []
temp_longest = [the_list[0]]

for i in range(1,len(the_list) + 1):
    current_object = the_list[i]
    if len(temp_longest)<1:
        temp_longest.append(current_object)

    if i > 0:
        if  temp_longest[i - 1] == current_object: #code won't work due to i - 1 being out of range
            temp_longest.append(current_object)
            if len(temp_longest) > len(longest_siquence):
                longest_siquence = temp_longest[:]
        else:
            temp_longest.clear()
print(longest_siquence)


    