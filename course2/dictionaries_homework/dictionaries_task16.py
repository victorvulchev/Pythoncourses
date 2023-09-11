competitors = {
 "George": 96,
 "Emily": 95,
 "Susan": 93,
 "Jane": 89,
 "Brett": 82
 }
'''for i in sorted_comp:
    rank_list.append(i)
print(rank_list)'''
sorted_comp = dict(sorted(competitors.items(), key=lambda item: item[1], reverse=True))
rank_list = []
dict_rank = sorted_comp.copy()


