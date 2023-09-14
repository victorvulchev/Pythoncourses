my_set1 = set([])
my_set2 = set([])

command = input("Enter a word or number:")
while command != "":
    my_set1.add(command)
    command = input("Enter a word or number:")
command = input("Enter a word or number:")
while command != "":
    my_set2.add(command)
    command = input("Enter a word or number:")
#sum = my_set1.difference(my_set2) + my_set2.difference(my_set1)
a = my_set1-my_set2
b = my_set2-my_set1
c = my_set1&my_set2
d= my_set1.union(my_set2)
my_set3 = set([])
my_set3.update(a,b,c,d)
print(a)
print(c)
print(my_set1)
print(my_set2)
print(my_set3)
print(d)