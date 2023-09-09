def parallelogram(input):
     a = input[0]
     b = input[1]
     h_a = input[2]
     area = a * h_a
     parameter = 2 * (a + b)
     print("area: " + str(area))
     print("parameter: "+ str(parameter))

parallelogram([5,4,6])