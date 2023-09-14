tup =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
new_list = sorted(tup, key=lambda x: x[1])
print(new_list)