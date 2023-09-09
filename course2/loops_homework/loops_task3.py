buff = ""

for i in range(5):
    buff += "* "
    print(buff)
for i in range(2,11,2):
    print(buff[:-i])