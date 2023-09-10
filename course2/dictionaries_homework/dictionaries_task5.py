d1 = {'a':1, 'b':2, 'd':3}
d2 = {'a':1, 'b':2, 'c':4} 
d3 = {}

for key in d1.keys():
    if key in d2:
        if d1[key] != d2[key]:
            d3[key] = [d1[key], d2[key]]
    else:
        d3[key] = ["None", d1[key]]
        for key in d2.keys():
            if key not in d1:
                d3[key] = ["None", d2[key]]
print(d3)

